#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import atexit
import shlex
import signal
import subprocess
import time
from typing import Dict, List


from comnetsemu.cli import CLI, spawnXtermDocker
from comnetsemu.net import Containernet, VNFManager
from mininet.log import info, setLogLevel
from mininet.node import Controller
from mininet.topo import Topo
from mininet.link import TCLink, TCIntf, Intf
from mininet.util import quietRun

class MyTopology(Topo):
    def build(self):
        self.addSwitch("rfsim5g-public")


if __name__ == "__main__":
    
    topo = MyTopology()

    AUTOTEST_MODE = os.environ.get("COMNETSEMU_AUTOTEST_MODE", 0)

    setLogLevel("info")
    
    working_directory="/home/vagrant/5G-NR-NTN/deploy_Core"
    
    #env = dict()
    #controller=Controller, link=Intf, waitConnected=True
    net = Containernet(topo=topo, controller=Controller)
    
    # set network bridge name
    bridge_name = "rfsim5g-public"
    
    # create the network bridge
    quietRun("docker network create --driver=bridge --subnet=192.168.71.128/26 --opt=com.docker.network.bridge.name={0} rfsim5g-oai-public-net".format(bridge_name))
    
    
    
    info("*** Adding Host for oai_nrf\n")
    #env["COMPONENT_NAME"]="oai_nrf"
    oai_nrf = net.addDockerHost(
        name="oai_nrf",
        dimage="oai-nrf-builder:develop",
        dcmd="bash /openair-nrf/bin/nrf-entrypoint.sh",
        ip="192.168.71.130/26",
        docker_args={
            "ports" : { "80/tcp": 3002,
                        "9090/tcp": 3003,
                       }, 
            "environment": {
                "TZ": "Europe/Paris",
                },
            "volumes": {
                working_directory + "/config_files/nrf.conf": {
                    "bind": "/openair-nrf/etc/nrf.conf",
                    "mode": "rw",
                },
                working_directory + "/entrypoints/nrf-entrypoint.sh": {
                    "bind": "/openair-nrf/bin/nrf-entrypoint.sh",
                    "mode": "rw",
                },
                working_directory + "/logs/nrf.log": {
                    "bind": "/openair-nrf/etc/nrf.log",
                    "mode": "rw",
                },
            },
        },
    )
    
    # env_nrf = {
    #     #"NRF_INTERFACE_NAME_FOR_SBI": "eth0",
    #     "TZ": "Europe/Paris",
    #     }
    # for var, value in env_nrf.items():
    #     oai_nrf.cmd('export {}={}'.format(var, value))
    
    # # Create Docker containers
    info("*** Adding Host for mysql\n")
    #env["COMPONENT_NAME"]="mysql"
    mysql = net.addDockerHost(
        name="mysql", 
        dimage="mysql:8.0",
        ip="192.168.71.131/26",
        #dcmd="bash /tmp/mysql-healthcheck.sh",
        docker_args={
            "ports" : { "3306/tcp": 3000,
                        "33060/tcp": 3001,
                       },  #"3306/tcp": {}, "33060/tcp": {}
            "environment": {
                "TZ": "Europe/paris",
                "MYSQL_DATABASE": "oai_db",
                "MYSQL_USER": "test",
                "MYSQL_PASSWORD": "test",
                "MYSQL_ROOT_PASSWORD": "linux",
                "restart": "always",
            },
            "healthcheck" : {
                "test": "/bin/bash -c /tmp/mysql-healthcheck.sh",
                "interval": 10000000000,
                "timeout": 5000000000,
                "retries": 5,
            },
            "volumes": {
                working_directory + "/healthchecks/oai_db.sql": {
                    "bind": "/docker-entrypoint-initdb.d/oai_db.sql",
                    "mode": "rw",
                },
                working_directory + "/healthchecks/mysql-healthcheck.sh": {
                    "bind": "/tmp/mysql-healthcheck.sh",
                    "mode": "rw",
                },
            },
        }, 
    )
    
    # Set environment variables using a dictionary
    # env_vars = {
    #     "TZ": "Europe/paris",
    #     "MYSQL_DATABASE": "oai_db",
    #     "MYSQL_USER": "test",
    #     "MYSQL_PASSWORD": "test",
    #     "MYSQL_ROOT_PASSWORD": "linux"
    #     }
    # for var, value in env_vars.items():
    #     mysql.cmd('export {}={}'.format(var, value))
    #mysql.setEnv(env_vars)
    
    # Run additional commands inside the container
    # mysql.cmd("apt-get update")
    # mysql.cmd("apt-get install -y iproute2")
    
    # info("*** Adding Host for oai_amf\n")
    # env["COMPONENT_NAME"]="oai_amf"
    # oai_amf = net.addDockerHost(
    #     name="oai_amf", 
    #     dimage="oai-amf-builder:develop",
    #     ip="192.168.71.132",
    #     dcmd="bash /openair-amf/bin/amf-entrypoint.sh",
    #     #dcmd = "/openair-amf/bin/amf-entrypoint.sh", # Define the command as a list of arguments
    #     #subprocess.call(dcmd), # Execute the command as an entry point
    #     docker_args={
    #         "environment": env,
    #         "volumes": {
    #             working_directory + "/config_files/amf.conf": {
    #                 "bind": "/openair-amf/etc/amf.conf",
    #                 "mode": "rw",
    #             },
    #             working_directory + "/entrypoints/amf-entrypoint.sh": {
    #                 "bind": "/openair-amf/bin/amf-entrypoint.sh",
    #                 "mode": "rw",
    #             },
    #             working_directory + "/logs/amf.log": {
    #                 "bind": "/openair-amf/etc/amf.log",
    #                 "mode": "rw",
    #             },
    #         },
    #     }, 
    # )
    
    # # Set environment variables using a dictionary
    # env_amf = {
    #     "TZ": "Europe/paris",
    #     "MCC": "208",
    #     "MNC": "99",
    #     "REGION_ID": "128",
    #     "AMF_SET_ID": "1",
    #     "SERVED_GUAMI_MCC_0": "208",
    #     "SERVED_GUAMI_MNC_0": "99",
    #     "SERVED_GUAMI_REGION_ID_0": "128",
    #     "SERVED_GUAMI_AMF_SET_ID_0": "1",
    #     "SERVED_GUAMI_MCC_1": "460",
    #     "SERVED_GUAMI_MNC_1": "11",
    #     "SERVED_GUAMI_REGION_ID_1": "10",
    #     "SERVED_GUAMI_AMF_SET_ID_1": "1",
    #     "PLMN_SUPPORT_MCC": "208",
    #     "PLMN_SUPPORT_MNC": "99",
    #     "PLMN_SUPPORT_TAC": "0x0001",
    #     "SST_0": "1",
    #     "AMF_INTERFACE_NAME_FOR_NGAP": "eth0",
    #     "AMF_INTERFACE_NAME_FOR_N11": "eth0",
    #     "SMF_INSTANCE_ID_0": "1",
    #     "SMF_FQDN_0": "oai-smf",
    #     "SMF_IPV4_ADDR_0": "192.168.71.133",
    #     "SELECTED_0": "true",
    #     "MYSQL_SERVER": "192.168.71.131",
    #     "MYSQL_USER": "root",
    #     "MYSQL_PASS": "linux",
    #     "MYSQL_DB": "oai_db",
    #     "NRF_IPV4_ADDRESS": "192.168.71.130",
    #     "NRF_FQDN": "oai-nrf",
    #     "NF_REGISTRATION": "yes",
    #     "SMF_SELECTION": "yes",
    #     "USE_FQDN_DNS": "yes",
    #     "USE_HTTP2": "no"
    #     }
    # for var, value in env_amf.items():
    #     oai_amf.cmd('export {}={}'.format(var, value))
    
    # info("*** Adding Host for oai_smf\n")
    # env["COMPONENT_NAME"]="oai_smf"
    # oai_smf = net.addDockerHost(
    #     name="oai_smf", 
    #     dimage="oai-smf-builder:develop",
    #     ip="192.168.71.133/26",
    #     dcmd="bash /openair-smf/bin/smf-entrypoint.sh",
    #     #dcmd = "/openair-smf/bin/smf-entrypoint.sh", # Define the command as a list of arguments
    #     #subprocess.call(dcmd), # Execute the command as an entry point
    #     docker_args={
    #         "environment": env,
    #         "volumes": {
    #             working_directory + "/config_files/smf.conf": {
    #                 "bind": "/openair-smf/etc/smf.conf",
    #                 "mode": "rw",
    #             },
    #             working_directory + "/entrypoints/smf-entrypoint.sh": {
    #                 "bind": "/openair-smf/bin/smf-entrypoint.sh",
    #                 "mode": "rw",
    #             },
    #             working_directory + "/logs/smf.log": {
    #                 "bind": "/openair-smf/etc/smf.log",
    #                 "mode": "rw",
    #             },
    #             # "/etc/timezone": {
    #             #     "bind": "/etc/timezone",
    #             #     "mode": "ro",
    #             # },
    #             # "/etc/localtime": {
    #             #     "bind": "/etc/localtime",
    #             #     "mode": "ro",
    #             # },
    #         },
    #     }, 
    # )
    
    # env_smf = {
    #     "TZ": "Europe/paris",
    #     "SMF_INTERFACE_NAME_FOR_N4": "eth0",
    #     "SMF_INTERFACE_NAME_FOR_SBI": "eth0",
    #     "DEFAULT_DNS_IPV4_ADDRESS": "172.21.3.100",
    #     "DEFAULT_DNS_SEC_IPV4_ADDRESS": "4.4.4.4",
    #     "AMF_IPV4_ADDRESS": "192.168.71.132",
    #     "AMF_FQDN": "oai-amf",
    #     "UPF_IPV4_ADDRESS": "192.168.71.134",
    #     "UPF_FQDN_0": "oai-spgwu",
    #     "NRF_IPV4_ADDRESS": "192.168.71.130",
    #     "NRF_FQDN": "oai-nrf",
    #     "REGISTER_NRF": "yes",
    #     "DISCOVER_UPF": "yes",
    #     "USE_FQDN_DNS": "yes",
    #     "USE_LOCAL_SUBSCRIPTION_INFO": "yes",
    #     "UE_MTU": "1500",
    #     "DNN_NI0": "oai",
    #     "TYPE0": "IPv4",
    #     "DNN_RANGE0": "12.1.1.2 - 12.1.1.127",
    #     "NSSAI_SST0": "1",
    #     "SESSION_AMBR_UL0": "200Mbps",
    #     "SESSION_AMBR_DL0": "400Mbps",
    #     "DEFAULT_CSCF_IPV4_ADDRESS": "127.0.0.1",
    #     "ENABLE_USAGE_REPORTING": "no"
    #     }
    # for var, value in env_smf.items():
    #     oai_smf.cmd('export {}={}'.format(var, value))
        
    
    # info("*** Adding Host for upf\n")
    # env["COMPONENT_NAME"]="oai_spgwu"
    # oai_spgwu = net.addDockerHost(
    #     name="oai_spgwu", 
    #     dimage="oai-spgwu-builder:develop",
    #     ip="192.168.71.134/26",
    #     dcmd="bash /openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
    #     #dcmd = "/openair-spgwu-tiny/bin/spgwu-entrypoint.sh", # Define the command as a list of arguments
    #     #subprocess.call(dcmd), # Execute the command as an entry point
    #     docker_args={
    #         "environment": env,
    #         "volumes": {
    #             working_directory + "/entrypoints/spgwu-entrypoint.sh": {
    #                 "bind": "/openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
    #                 "mode": "rw",
    #             },
    #             working_directory + "/config_files/spgw_u.conf": {
    #                 "bind": "/openair-spgwu-tiny/etc/spgw_u.conf",
    #                 "mode": "rw",
    #             },
    #             working_directory + "/logs/spgw_u.log": {
    #                 "bind": "/openair-spgwu-tiny/etc/spgw_u.log",
    #                 "mode": "rw",
    #             },
    #             # "/etc/timezone": {
    #             #     "bind": "/etc/timezone",
    #             #     "mode": "ro",
    #             # },
    #             # "/etc/localtime": {
    #             #     "bind": "/etc/localtime",
    #             #     "mode": "ro",
    #             # },
    #         },
    #         "cap_add": ["NET_ADMIN", "SYS_ADMIN"]
    #     }, 
    # )
    
    # # Set environment variables using a dictionary
    # env_spgwu = {
    #     "TZ": "Europe/Paris",
    #     "SGW_INTERFACE_NAME_FOR_S1U_S12_S4_UP": "eth0",
    #     "SGW_INTERFACE_NAME_FOR_SX": "eth0",
    #     "PGW_INTERFACE_NAME_FOR_SGI": "eth0",
    #     "NETWORK_UE_NAT_OPTION": "yes",
    #     "NETWORK_UE_IP": "12.1.1.0/24",
    #     "ENABLE_5G_FEATURES": "yes",
    #     "REGISTER_NRF": "yes",
    #     "USE_FQDN_NRF": "yes",
    #     "UPF_FQDN_5G": "oai-spgwu",
    #     "NRF_IPV4_ADDRESS": "192.168.71.130",
    #     "NRF_FQDN": "oai-nrf",
    #     # Only one slice is defined (1, 0xFFFFFF)
    #     "NSSAI_SST_0": "1",
    #     "NSSAI_SD_0": "0xffffff",
    #     "DNN_0": "oai"
    #     }
    # for var, value in env_spgwu.items():
    #     oai_spgwu.cmd('export {}={}'.format(var, value))
    
    
    
   
    
    # # Add contrller
    # info("*** Adding controller\n")
    # net.addController("c0")

    # # # Add switches
    # info("*** Adding switches\n")
    # s1 = net.addSwitch('s1')
    # s2 = net.addSwitch('s2')
    # # s3 = net.addSwitch('s3')
    # # s4 = net.addSwitch('s4')
    # # s5 = net.addSwitch('s5')

    # Add links
    #info("*** Adding links\n")
    #net.addLink(s1,  s2)
    # net.addLink(s2,  s3, bw=1000, delay="50ms", intfName1="s2-s3",  intfName2="s3-s2")
    # net.addLink(s3,  s4, bw=1000, delay="50ms", intfName1="s3-s4",  intfName2="s4-s3")
    # net.addLink(s4,  s5, bw=1000, delay="50ms", intfName1="s4-s5",  intfName2="s5-s4")
    # net.addLink(mysql, oai_nrf)
    # net.addLink(oai_nrf, oai_amf)
    # net.addLink(oai_nrf, oai_smf)
    #net.addLink(mysql, s2, bw=10, delay="1ms", intfName1="mysql-s2",  intfName2="s2-mysql")
    # net.addLink(oai_amf, s3, bw=1000, delay="10ms", intfName1="oai_amf-s3",  intfName2="s3-oai_amf")
    # net.addLink(oai_smf, s4, bw=1000, delay="10ms", intfName1="oai_smf-s4",  intfName2="s4-oai_smf")
    # net.addLink(oai_spgwu, s5, bw=1000, delay="10ms", intfName1="oai_spgwu-s5",  intfName2="s5-oai_spgwu")
    
    
    # Connect containers to the network bridge
    # net.addLink(oai_nrf, bridge_name, intfName1='oai_nrf-eth0', intfName2='rfsim5g-public-eth1')
    # net.addLink(mysql, bridge_name, intfName1='mysql-eth0', intfName2='rfsim5g-public-eth2')
    
     # Connect containers to the existing network bridge
    oai_nrf.cmd("ip link add oai_nrf-eth0 type veth peer name rfsim5g-public-eth1")
    oai_nrf.cmd("ip link set oai_nrf-eth0 up")
    oai_nrf.cmd("brctl addif rfsim5g-public oai_nrf-eth0")

    mysql.cmd("ip link add mysql-eth0 type veth peer name rfsim5g-public-eth2")
    mysql.cmd("ip link set mysql-eth0 up")
    mysql.cmd("brctl addif rfsim5g-public mysql-eth0")
    
    
    #Start the network
    info("\n*** starting network\n")
    net.start()

if not AUTOTEST_MODE:
        CLI(net)
        net.stop()