import os
import time


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
    
    working_directory="/home/ubuntu/5G-NR-NTN/openairinterface5g"
    
    env = dict()
    
    net = Containernet(controller=Controller, link=TCLink, waitConnected=True)


    # Create Docker containers
    info("*** Adding Host for oai-nrf\n")
    env["COMPONENT_NAME"]="oai_nrf"
    oai_nrf = net.addDockerHost(
        name="oai_nrf",
        dimage="oaisoftwarealliance/oai-nrf:v1.5.0",
        #dcmd="bash /openair-nrf/bin/nrf-entrypoint.sh",
        ip="192.168.71.130/26",
        docker_args={
            "environment": env,
            "volumes": {
                working_directory + "/deploy-core/config_files/nrf.conf": {
                    "bind": "/openair-nrf/etc/nrf.conf",
                    "mode": "rw",
                },
                # working_directory + "/deploy-core/entrypoints/nrf-entrypoint.sh": {
                #     "bind": "/openair-nrf/bin/nrf-entrypoint.sh",
                #     "mode": "rw",
                # }
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
        )
    
    # mysql = net.addHost('mysql', cls=Docker, ip='192.168.71.131', dimage='mysql:8.0')
    # oai_amf = net.addHost('oai-amf', cls=Docker, ip='192.168.71.132', dimage='oaisoftwarealliance/oai-amf:v1.5.0')
    # oai_smf = net.addHost('oai-smf', cls=Docker, ip='192.168.71.133', dimage='oaisoftwarealliance/oai-smf:v1.5.0')
    # oai_spgwu = net.addHost('oai-spgwu', cls=Docker, ip='192.168.71.134', dimage='oaisoftwarealliance/oai-spgwu-tiny:v1.5.0')
    # oai_ext_dn = net.addHost('oai-ext-dn', cls=Docker, ip='192.168.72.135', dimage='oaisoftwarealliance/trf-gen-cn5g:focal')
    # oai_cu = net.addHost('oai-cu', cls=Docker, ip='192.168.71.140', dimage='oaisoftwarealliance/oai-gnb:develop')
    # oai_du = net.addHost('oai-du', cls=Docker, ip='192.168.71.142', dimage='oaisoftwarealliance/oai-gnb:develop')
    # oai_nr_ue = net.addHost('oai-nr-ue', cls=Docker, ip='192.168.71.150', dimage='oaisoftwarealliance/oai-nr-ue:develop')
    # oai_nr_ue2 = net.addHost('oai-nr-ue2', cls=Docker, ip='192.168.71.151', dimage='oaisoftwarealliance/oai-nr-ue:develop')
    
    # Add contrller
    info("*** Adding controller\n")
    net.addController("c0")

    # Add switches
    info("*** Adding switches\n")
    s1 = net.addSwitch('s1')
    # switch2 = net.addSwitch('switch2')
    # switch3 = net.addSwitch('switch3')
    # switch4 = net.addSwitch('switch4')

    # Add links
    info("*** Adding links\n")
    net.addLink(oai_nrf, s1, bw=1000, delay="10ms", intfName1="oai_nrf-s1",  intfName2="s1-oai_nrf")
    # net.addLink(mysql, switch1)
    # net.addLink(oai_amf, switch1)
    # net.addLink(oai_smf, switch1)
    # net.addLink(oai_spgwu, switch1)
    # net.addLink(oai_ext_dn, switch2)
    # net.addLink(oai_cu, switch3)
    # net.addLink(oai_du, switch3)
    # net.addLink(oai_nr_ue, switch4)
    # net.addLink(oai_nr_ue2, switch4)
    
    #Start the network
    info("\n*** starting network\n")
    net.start()

if not AUTOTEST_MODE:
        CLI(net)
        net.stop()