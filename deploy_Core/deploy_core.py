import os
import time
import subprocess


from comnetsemu.cli import CLI, spawnXtermDocker
from comnetsemu.net import Containernet, VNFManager
#from mininet.net import Mininet
from mininet.log import info, setLogLevel
#from mininet.node import Docker
from mininet.node import Controller
#from mininet.node import Controller, RemoteController, OVSBridge, OVSKernelSwitch
from mininet.topo import Topo
from mininet.link import TCLink

if __name__ == "__main__":

    AUTOTEST_MODE = os.environ.get("COMNETSEMU_AUTOTEST_MODE", 0)

    setLogLevel("info")
    
    working_directory="/home/ubuntu/5G-NR-NTN/openairinterface5g/deploy_Core"
    
    env = dict()
    # Set environment variables
    env["TZ"] = "Europe/Paris"
    env["MYSQL_DATABASE"] = "oai_db"
    env["MYSQL_USER"] = "test"
    env["MYSQL_PASSWORD"] = "test"
    env["MYSQL_ROOT_PASSWORD"] = "linux"
    
    net = Containernet(controller=Controller, link=TCLink, waitConnected=True)


    # Create Docker containers
    info("*** Adding Host for rfsim5g-mysql\n")
    env["COMPONENT_NAME"]="mysql"
    mysql = net.addDockerHost(
        name="mysql", 
        dimage="mysql:8.0",
        ip="192.168.71.131/26",
        docker_args={
            "environment": env,
            "volumes": {
                working_directory + "/oai_db.sql": {
                    "bind": "/docker-entrypoint-initdb.d/oai_db.sql",
                    "mode": "rw",
                },
                working_directory + "/healthchecks/mysql-healthcheck.sh": {
                    "bind": "/tmp/mysql-healthcheck.sh",
                    "mode": "rw",
                },
                "/etc/timezone": {
                    "bind": "/etc/timezone",
                    "mode": "ro",
                },
                "/etc/localtime": {
                    "bind": "/etc/localtime",
                    "mode": "ro",
                },
            },
        }, 
    )
    
    info("*** Adding Host for oai-nrf\n")
    env["COMPONENT_NAME"]="oai_nrf"
    oai_nrf = net.addDockerHost(
        name="oai_nrf",
        dimage="oai-nrf:v1.5.0",
        command = "/openair-nrf/bin/nrf-entrypoint.sh", # Define the command as a list of arguments
        ip="192.168.71.130/26",
        docker_args={
            "environment": env,
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
                "/etc/timezone": {
                    "bind": "/etc/timezone",
                    "mode": "ro",
                },
                "/etc/localtime": {
                    "bind": "/etc/localtime",
                    "mode": "ro",
                },
            },
        },
        #subprocess.call(command) # Execute the command as an entry point
        )
    
    info("*** Adding Host for oai_amf\n")
    env["COMPONENT_NAME"]="oai_amf"
    oai_amf = net.addDockerHost(
        name="oai_amf", 
        dimage="oai-amf:v1.5.0",
        ip="192.168.71.132/26",
        command = "/openair-amf/bin/amf-entrypoint.sh", # Define the command as a list of arguments
        docker_args={
            "environment": env,
            "volumes": {
                working_directory + "/config_files/amf.conf": {
                    "bind": "/openair-amf/etc/amf.conf",
                    "mode": "rw",
                },
                working_directory + "/entrypoints/amf-entrypoint.sh": {
                    "bind": "/openair-amf/bin/amf-entrypoint.sh",
                    "mode": "rw",
                },
                working_directory + "/logs/amf.log": {
                    "bind": "/openair-amf/etc/amf.log",
                    "mode": "rw",
                },
                "/etc/timezone": {
                    "bind": "/etc/timezone",
                    "mode": "ro",
                },
                "/etc/localtime": {
                    "bind": "/etc/localtime",
                    "mode": "ro",
                },
            },
        }, 
    )
    
    info("*** Adding Host for oai_smf\n")
    env["COMPONENT_NAME"]="oai_smf"
    oai_smf = net.addDockerHost(
        name="oai_smf", 
        dimage="oai-smf:v1.5.0",
        ip="192.168.71.133/26",
        command = "/openair-smf/bin/smf-entrypoint.sh", # Define the command as a list of arguments
        docker_args={
            "environment": env,
            "volumes": {
                working_directory + "/config_files/smf.conf": {
                    "bind": "/openair-smf/etc/smf.conf",
                    "mode": "rw",
                },
                working_directory + "/entrypoints/smf-entrypoint.sh": {
                    "bind": "/openair-smf/bin/smf-entrypoint.sh",
                    "mode": "rw",
                },
                working_directory + "/logs/smf.log": {
                    "bind": "/openair-smf/etc/smf.log",
                    "mode": "rw",
                },
                "/etc/timezone": {
                    "bind": "/etc/timezone",
                    "mode": "ro",
                },
                "/etc/localtime": {
                    "bind": "/etc/localtime",
                    "mode": "ro",
                },
            },
        }, 
    )
    
    info("*** Adding Host for upf\n")
    env["COMPONENT_NAME"]="oai_spgwu"
    oai_spgwu = net.addDockerHost(
        name="oai_spgwu", 
        dimage="oai-spgwu:v1.5.0",
        ip="192.168.71.134/26",
        command = "/openair-spgwu-tiny/bin/spgwu-entrypoint.sh", # Define the command as a list of arguments
        docker_args={
            "environment": env,
            "volumes": {
                working_directory + "/entrypoints/spgwu-entrypoint.sh": {
                    "bind": "/openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
                    "mode": "rw",
                },
                working_directory + "/config_files/spgw_u.conf": {
                    "bind": "/openair-spgwu-tiny/etc/spgw_u.conf",
                    "mode": "rw",
                },
                working_directory + "/logs/spgw_u.log": {
                    "bind": "/openair-spgwu-tiny/etc/spgw_u.log",
                    "mode": "rw",
                },
                "/etc/timezone": {
                    "bind": "/etc/timezone",
                    "mode": "ro",
                },
                "/etc/localtime": {
                    "bind": "/etc/localtime",
                    "mode": "ro",
                },
            },
        }, 
    )
    
    
    
    
    
   
    
    # Add contrller
    info("*** Adding controller\n")
    net.addController("c0")

    # Add switches
    info("*** Adding switches\n")
    s1 = net.addSwitch('s1')
    # s2 = net.addSwitch('s2')
    # s3 = net.addSwitch('s3')
    # s4 = net.addSwitch('s4')
    # s5 = net.addSwitch('s5')

    # Add links
    info("*** Adding links\n")
    net.addLink(mysql, s1, bw=1000, delay="10ms", intfName1="mysql-s1",  intfName2="s1-mysql")
    net.addLink(oai_nrf, s1, bw=1000, delay="10ms", intfName1="oai_nrf-s1",  intfName2="s1-oai_nrf")
    net.addLink(oai_amf, s1, bw=1000, delay="10ms", intfName1="oai_amf-s1",  intfName2="s1-oai_amf")
    net.addLink(oai_smf, s1, bw=1000, delay="10ms", intfName1="oai_smf-s1",  intfName2="s1-oai_smf")
    net.addLink(oai_spgwu, s1, bw=1000, delay="10ms", intfName1="oai_spgwu-s1",  intfName2="s1-oai_spgwu")
   
    
    #Start the network
    info("\n*** starting network\n")
    net.start()

if not AUTOTEST_MODE:
        CLI(net)
        net.stop()