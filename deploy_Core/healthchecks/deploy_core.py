#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import atexit
import shlex
import signal
import subprocess
import time
from typing import Dict, List

import comnetsemu
from comnetsemu.cli import CLI, spawnXtermDocker
from comnetsemu.net import Containernet, VNFManager
from mininet.log import info, setLogLevel
from mininet.node import Controller, OVSKernelSwitch, UserSwitch
from mininet.topo import Topo
from mininet.link import TCLink, TCIntf, Intf
from mininet.util import quietRun


if __name__ == "__main__":

    AUTOTEST_MODE = os.environ.get("COMNETSEMU_AUTOTEST_MODE", 0)

    setLogLevel("info")
    
    working_directory="/home/henok/5G-NR-NTN"
    
    env = dict()
    net = Containernet() #controller=Controller, link=TCLink, switch=OVSKernelSwitch
    
    
    info("*** Adding Host for rfsim5g-oai-nrf\n")
    oainrf = net.addDockerHost(
        "oainrf",
        dimage="oai-nrf:develop",
        ip="192.168.71.130/26",
        #mac="00:00:00:00:00:01",
        dcmd="/bin/bash /openair-nrf/bin/nrf-entrypoint.sh",
        docker_args={
            #"ports" : {"80/tcp": 80, "8080/tcp": 8080}, 
            "environment": {"NRF_INTERFACE_NAME_FOR_SBI":"eth0", "TZ":"Europe/Paris"},
            "volumes": {
                working_directory + "/deploy_Core/config_files/nrf.conf": {
                    "bind": "/openair-nrf/etc/nrf.conf",
                },
                working_directory + "/deploy_Core/entrypoints/nrf-entrypoint.sh": {
                    "bind": "/openair-nrf/bin/nrf-entrypoint.sh",
                },
                working_directory + "/deploy_Core/logs/nrf.log": {
                    "bind": "/openair-nrf/etc/nrf.log",
                    "mode": "rw",
                },
            },
        },
    )
    
    
    # # Create Docker containers
    info("*** Adding Host for mysql\n")
    mysql = net.addDockerHost(
        "mysql", 
        dimage="mysql:8.0",
        #mac="00:00:00:00:00:02",
        ip="192.168.71.131/26",
        docker_args={
            "environment": {"TZ":"Europe/paris", "MYSQL_DATABASE":"oai_db", "MYSQL_USER":"test", "MYSQL_PASSWORD":"test", "MYSQL_ROOT_PASSWORD":"linux"},
            "ports" : {"3306/tcp": 3306, "33060/tcp": 33060}, 
            "volumes": {
                working_directory + "/deploy_Core/healthchecks/oai_db.sql": {
                    "bind": "/docker-entrypoint-initdb.d/oai_db.sql",
                },
                working_directory + "/deploy_Core/healthchecks/mysql-healthcheck.sh": {
                    "bind": "/tmp/mysql-healthcheck.sh",
                },
            },
            "healthcheck" : {
                "test": "/bin/bash -c /tmp/mysql-healthcheck.sh",
                "interval": 10000000000,
                "timeout": 5000000000,
                "retries": 30,
            },
        }, 
    )
    
    # Create a direct link between the hosts
    link = net.addLink(oainrf, mysql)
    
    # info("*** Add controller\n")
    # net.addController("c0")

    # info("*** Adding switch\n")
    # s1 = net.addSwitch("s1")
    # s2 = net.addSwitch("s2")
    
    # info("*** Adding links\n")
    # net.addLink(s1, s2)
    # net.addLink(s1, s2)
    # net.addLink(s1, s2)
    
    #Start the network
    info("\n*** starting network\n")
    net.start()

if not AUTOTEST_MODE:
    CLI(net)
    net.stop()