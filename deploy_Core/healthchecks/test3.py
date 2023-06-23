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
        self.addSwitch("rfsim5g-traffic")


if __name__ == "__main__":
    
    topo = MyTopology()

    AUTOTEST_MODE = os.environ.get("COMNETSEMU_AUTOTEST_MODE", 0)

    setLogLevel("info")
    
    working_directory="/home/henok/5G-NR-NTN"
    
    env = dict()
    #controller=Controller, link=Intf, waitConnected=True
    net = Containernet(topo=topo, controller=Controller)
    
    # set network bridge name
    bridge_name1 = "rfsim5g-public"
    bridge_name2 = "rfsim5g-traffic"
    
    # create the network bridge
    quietRun("docker network create --driver=bridge --subnet=192.168.71.128/26 --opt=com.docker.network.bridge.name={0} rfsim5g-oai-public-net".format(bridge_name1))
    quietRun("docker network create --driver=bridge --subnet=192.168.72.128/26 --opt=com.docker.network.bridge.name={0} rfsim5g-oai-traffic_net-net".format(bridge_name2))
    
    
    info("*** Adding Host for oai_nrf\n")
    #env["COMPONENT_NAME"]="oai-nrf"
    oai_nrf = net.addDockerHost(
        name="rfsim5g-oai-nrf",
        dimage="oaisoftwarealliance/oai-nrf:v1.5.0",
        ip="192.168.71.130",
        #dcmd="/bin/bash /openair-nrf/bin/nrf-entrypoint.sh",
        docker_args={
            "ports" : {
                "80/tcp": 3002,
                "9090/tcp": 3003,
                }, 
            "environment": {
                "NRF_INTERFACE_NAME_FOR_SBI": "eth0",
                "TZ": "Europe/Paris",
                },
            # "volumes": {
            #     working_directory + "/deploy_Core/config_files/nrf.conf": {
            #         "bind": "/openair-nrf/etc/nrf.conf",
            #     },
            #     working_directory + "/deploy_Core/entrypoints/nrf-entrypoint.sh": {
            #         "bind": "/openair-nrf/bin/nrf-entrypoint.sh",
            #     },
            #     working_directory + "/deploy_Core/logs/nrf.log": {
            #         "bind": "/openair-nrf/etc/nrf.log",
            #         "mode": "rw",
            #     },
            # },
        },
    )
    
    
    # # Create Docker containers
    info("*** Adding Host for mysql\n")
    #env["COMPONENT_NAME"]="mysql"
    mysql = net.addDockerHost(
        name="rfsim5g-mysql", 
        dimage="mysql:8.0",
        ip="192.168.71.131",
        #dcmd="/bin/bash -c /tmp/mysql-healthcheck.sh",
        docker_args={
            "ports" : {
                "3306/tcp": 3001,
                "33060/tcp": 3004,
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
                "retries": 30,
            },
            "volumes": {
                working_directory + "/deploy_Core/healthchecks/oai_db.sql": {
                    "bind": "/docker-entrypoint-initdb.d/oai_db.sql",
                },
                working_directory + "/deploy_Core/healthchecks/mysql-healthcheck.sh": {
                    "bind": "/tmp/mysql-healthcheck.sh",
                },
            },
        }, 
    )
    
    info("*** Adding Host for oai_amf\n")
    #env["COMPONENT_NAME"]="oai-amf"
    oai_amf = net.addDockerHost(
        name="rfsim5g-oai-amf", 
        dimage="oaisoftwarealliance/oai-amf:v1.5.0",
        ip="192.168.71.132",
        #dcmd="/bin/bash /openair-amf/bin/amf-entrypoint.sh",
        docker_args={
            "ports" : {
                "80/tcp": 3005,
                "9090/tcp": 3006,
                "38412/sctp": 3007,
                },
            "environment": {
                "TZ": "Europe/paris",
                "MCC": "208",
                "MNC": "99",
                "REGION_ID": "128",
                "AMF_SET_ID": "1",
                "SERVED_GUAMI_MCC_0": "208",
                "SERVED_GUAMI_MNC_0": "99",
                "SERVED_GUAMI_REGION_ID_0": "128",
                "SERVED_GUAMI_AMF_SET_ID_0": "1",
                "SERVED_GUAMI_MCC_1": "460",
                "SERVED_GUAMI_MNC_1": "11",
                "SERVED_GUAMI_REGION_ID_1": "10",
                "SERVED_GUAMI_AMF_SET_ID_1": "1",
                "PLMN_SUPPORT_MCC": "208",
                "PLMN_SUPPORT_MNC": "99",
                "PLMN_SUPPORT_TAC": "0x0001",
                "SST_0": "1",
                "AMF_INTERFACE_NAME_FOR_NGAP": "eth0",
                "AMF_INTERFACE_NAME_FOR_N11": "eth0",
                "SMF_INSTANCE_ID_0": "1",
                "SMF_FQDN_0": "oai-smf",
                "SMF_IPV4_ADDR_0": "192.168.71.133",
                "SELECTED_0": "true",
                "MYSQL_SERVER": "mysql",
                "MYSQL_USER": "test",
                "MYSQL_PASS": "test",
                "MYSQL_DB": "oai_db",
                "NRF_IPV4_ADDRESS": "192.168.71.130",
                "NRF_FQDN": "oai-nrf",
                "NF_REGISTRATION": "yes",
                "SMF_SELECTION": "yes",
                "USE_FQDN_DNS": "yes",
                "USE_HTTP2": "yes"
            },
            # "volumes": {
            #     working_directory + "/deploy_Core/config_files/amf.conf": {
            #         "bind": "/openair-amf/etc/amf.conf",
            #         "mode": "rw",
            #     },
            #     working_directory + "/deploy_Core/entrypoints/amf-entrypoint.sh": {
            #         "bind": "/openair-amf/bin/amf-entrypoint.sh",
            #         "mode": "rw",
            #     },
            #     working_directory + "/deploy_Core/logs/amf.log": {
            #         "bind": "/openair-amf/etc/amf.log",
            #         "mode": "rw",
            #     },
            # },
        }, 
    )
    
    info("*** Adding Host for oai_smf\n")
    #env["COMPONENT_NAME"]="oai-smf"
    oai_smf = net.addDockerHost(
        name="rfsim5g-oai-smf", 
        dimage="oaisoftwarealliance/oai-smf:v1.5.0",
        ip="192.168.71.133",
        #dcmd="/bin/bash /openair-smf/bin/smf-entrypoint.sh",
        docker_args={
            "ports" : {
                "80/tcp": 3008,
                "9090/tcp": 3009,
                "8805/udp": 3010, # 80/tcp, 8805/udp, 9090/tcp
                },
            "environment": {
                "TZ": "Europe/paris",
                "SMF_INTERFACE_NAME_FOR_N4": "eth0",
                "SMF_INTERFACE_NAME_FOR_SBI": "eth0",
                "DEFAULT_DNS_IPV4_ADDRESS": "172.21.3.100",
                "DEFAULT_DNS_SEC_IPV4_ADDRESS": "4.4.4.4",
                "AMF_IPV4_ADDRESS": "192.168.71.132",
                "AMF_FQDN": "localhost",
                "UPF_IPV4_ADDRESS": "192.168.71.134",
                "UPF_FQDN_0": "localhost",
                "NRF_IPV4_ADDRESS": "192.168.71.130",
                "NRF_FQDN": "localhost",
                "REGISTER_NRF": "yes",
                "DISCOVER_UPF": "yes",
                "USE_FQDN_DNS": "yes",
                "USE_LOCAL_SUBSCRIPTION_INFO": "yes",
                "UE_MTU": "1500",
                "DNN_NI0": "oai",
                "TYPE0": "IPv4",
                "DNN_RANGE0": "12.1.1.2 - 12.1.1.127",
                "NSSAI_SST0": "1",
                "SESSION_AMBR_UL0": "200Mbps",
                "SESSION_AMBR_DL0": "400Mbps",
                "DEFAULT_CSCF_IPV4_ADDRESS": "127.0.0.1",
                "ENABLE_USAGE_REPORTING": "no",
            },
            # "volumes": {
            #     working_directory + "/deploy_Core/config_files/smf.conf": {
            #         "bind": "/openair-smf/etc/smf.conf",
            #     },
            #     working_directory + "/deploy_Core/entrypoints/smf-entrypoint.sh": {
            #         "bind": "/openair-smf/bin/smf-entrypoint.sh",
            #     },
            #     working_directory + "/deploy_Core/logs/smf.log": {
            #         "bind": "/openair-smf/etc/smf.log",
            #         "mode": "rw",
            #     },
            # },
        }, 
    )
        
    
    info("*** Adding Host for upf\n")
    oai_spgwu = net.addDockerHost(
        name="rfsim5g-oai-spgwu", 
        dimage="oaisoftwarealliance/oai-spgwu-tiny:v1.5.0",
        ip="192.168.71.134/24",
        #dcmd = "/bin/bash /openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
        #dcmd="exec /openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
        docker_args={
            "ports" : { "2152/udp": 3011,
                        "8805/udp": 3012,
                       },   #2152/udp, 8805/udp
            "environment": {
                "TZ": "Europe/Paris",
                "SGW_INTERFACE_NAME_FOR_S1U_S12_S4_UP": "eth0",
                "SGW_INTERFACE_NAME_FOR_SX": "eth0",
                "PGW_INTERFACE_NAME_FOR_SGI": "eth0",
                "NETWORK_UE_NAT_OPTION": "yes",
                "NETWORK_UE_IP": "12.1.1.0/24",
                "ENABLE_5G_FEATURES": "yes",
                "REGISTER_NRF": "yes",
                "USE_FQDN_NRF": "yes",
                "UPF_FQDN_5G": "oai-spgwu",
                "NRF_IPV4_ADDRESS": "192.168.71.130",
                "NRF_FQDN": "localhost",
                # Only one slice is defined (1, 0xFFFFFF)
                "NSSAI_SST_0": "1",
                "NSSAI_SD_0": "0xffffff",
                "DNN_0": "oai",   
            },
            # "volumes": {
            #     working_directory + "/deploy_Core/entrypoints/spgwu-entrypoint.sh": {
            #         "bind": "/openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
            #         "mode": "rw",
            #     },
            #     working_directory + "/deploy_Core/config_files/spgw_u.conf": {
            #         "bind": "/openair-spgwu-tiny/etc/spgw_u.conf",
            #         "mode": "rw",
            #     },
            #     working_directory + "/deploy_Core/logs/spgw_u.log": {
            #         "bind": "/openair-spgwu-tiny/etc/spgw_u.log",
            #         "mode": "rw",
            #     },
            # },
            "cap_add": ["NET_ADMIN", "SYS_ADMIN"],
            "cap_drop": "ALL",
        },
    )
    
    info("*** Adding Host for traffic_generator\n")
    oai_ext_dn = net.addDockerHost(
        name="rfsim5g-oai-ext-dn", 
        #privileged: "true",
        dimage="oaisoftwarealliance/trf-gen-cn5g:focal",
        ip="192.168.72.135",
        # Add a Docker host with the specified entry point
        dcmd = "/bin/bash -c 'iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE; \
            ip route add 12.1.1.0/24 via 192.168.72.134 dev eth0; sleep infinity'",
        #dcmd="/bin/bash -c "iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE;", "ip route add 12.1.1.0/24 via 192.168.72.134 dev eth0; sleep infinity",
        #dcmd=["/bin/bash -c iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE", "ip route add 12.1.1.0/24 via 192.168.72.134 dev eth0", "sleep infinity"],
        docker_args={
            "healthcheck" : {
                "test": "/bin/bash -c ping -c 2 192.168.72.134",
                "interval": 10000000000,
                "timeout": 5000000000,
                "retries": 5,
            },
        }, 
    )
    
    info("*** Adding Host for gNB-CU\n")
    oai_cu = net.addDockerHost(
        name="rfsim5g-oai-cu", 
        dimage="oaisoftwarealliance/oai-gnb:develop",
        ip="192.168.71.140",
        docker_args={
            "ports" : {
                "4043/tcp": 3013,
            },
            "environment": {
                "TZ": "Europe/Paris",
                # "RFSIMULATOR": "server",
                # "USE_ADDITIONAL_OPTIONS": "--sa --rfsim --log_config.global_log_options level,nocolor,time",
            },
            "volumes": {
                working_directory + "/deploy_RAN/openairinterface5g/ci-scripts/conf_files/gnb-cu.sa.band78.106prb.conf": {
                    "bind": "/opt/oai-gnb/etc/gnb.conf",
                    #"mode": "rw",
                },
            },
            "healthcheck" : {
                "test": "/bin/bash -c pgrep nr-softmodem",
                "interval": 10000000000,
                "timeout": 5000000000,
                "retries": 5,
            },
        },
    )
    
    info("*** Adding Host for gNB-DU\n")
    oai_du = net.addDockerHost(
        name="rfsim5g-oai-du", 
        dimage="oaisoftwarealliance/oai-gnb:develop",
        ip="192.168.71.142",
        docker_args={
            "ports" : {
                "4043/tcp": 3014,
            },
            "environment": {
                "TZ": "Europe/Paris",
                # "RFSIMULATOR": "server",
                # "USE_ADDITIONAL_OPTIONS": "--sa --rfsim --log_config.global_log_options level,nocolor,time",  
            },
            "volumes": {
                working_directory + "/deploy_RAN/openairinterface5g/ci-scripts/conf_files/gnb-du.sa.band78.106prb.rfsim.conf": {
                    "bind": "/opt/oai-gnb/etc/gnb.conf",
                    #"mode": "rw",
                },
            },
            "healthcheck" : {
                "test": "/bin/bash -c pgrep nr-softmodem",
                "interval": 10000000000,
                "timeout": 5000000000,
                "retries": 5,
            },
        },
    )
    
    info("*** Adding Host for NR-UE\n")
    oai_nr_ue = net.addDockerHost(
        name="rfsim5g-oai-nr-ue", 
        dimage="oaisoftwarealliance/oai-nr-ue:develop",
        ip="192.168.71.150",
        docker_args={
            "environment": {
                "TZ": "Europe/Paris",
                # "RFSIMULATOR": "192.168.71.142",
                # "USE_ADDITIONAL_OPTIONS": "--sa --rfsim -r 106 --numerology 1 --uicc0.imsi 208990100001100 -C 3619200000 --log_config.global_log_options level,nocolor,time", 
            },
            "volumes": {
                working_directory + "/deploy_RAN/openairinterface5g/ci-scripts/conf_files/nrue.uicc.conf": {
                    "bind": "/opt/oai-nr-ue/etc/nr-ue.conf",
                },
            },
            "healthcheck" : {
                "test": "/bin/bash -c pgrep nr-softmodem",
                "interval": 10000000000,
                "timeout": 5000000000,
                "retries": 5,
            },
        },
    )
    
    
    #Start the network
    info("\n*** starting network\n")
    net.start()

if not AUTOTEST_MODE:
        CLI(net)
        net.stop()