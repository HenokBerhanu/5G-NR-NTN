import atexit
import os
import shlex
import signal
import subprocess
import time
from typing import Dict, List

from comnetsemu.cli import CLI, spawnXtermDocker
from comnetsemu.net import Containernet, VNFManager
from comnetsemu.node import DockerHost
from mininet.link import TCLink, TCIntf, Intf
from mininet import log
from mininet.log import info, setLogLevel
from mininet.node import Controller, RemoteController, OVSBridge, OVSKernelSwitch
from mininet.topo import Topo

root_directory="/home/henok/5G-NR-NTN/deploy_Core"


if __name__ == "__main__":

    AUTOTEST_MODE = os.environ.get("COMNETSEMU_AUTOTEST_MODE", 0)

    setLogLevel("info")
    

    env = dict()
    
    net = Containernet(controller=Controller, link=TCLink)

    # cmds: Dict[DockerHost, str] = {}
    # hardcoded_ips: List[Dict[str, str]] = []

    info("*** Adding Host for upf\n")
    env["COMPONENT_NAME"]="rfsim5g-oai-spgwu"
    oaispgwu = net.addDockerHost(
        "rfsim5g-oai-spgwu", 
        dimage="oaisoftwarealliance/oai-spgwu-tiny:v1.5.0",
        ip="192.168.71.134/26",
        #ip="192.168.72.134",
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
            #     # working_directory + "/deploy_Core/entrypoints/spgwu-entrypoint.sh": {
            #     #     "bind": "/openair-spgwu-tiny/bin/spgwu-entrypoint.sh",
            #     #     "mode": "rw",
            #     # },
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
            "sysctls": {"net.ipv4.ip_forward": 1},
            #"devices": "/dev/net/tun:/dev/net/tun:rwm",
        },
    )

    # info("*** Adding Host for SRSRAN UE\n")
    # env["COMPONENT_NAME"]="srsue"
    # srsue = net.addDockerHost(
    #     "srsue",
    #     dimage="srsran3",
    #     ip="192.168.0.30/24",
    #     exec_run = "/etc/srsran/ue.conf",
    #     docker_args={
    #         "environment": env,
    #         "volumes": {
    #             root_directory + "/srsran/config": {
    #                 "bind": "/etc/srsran",
    #                 "mode": "rw",
    #             },
    #             root_directory + "/srslogs": {
    #                 "bind": "/tmp/srsran_logs",
    #                 "mode": "rw",
    #             },
    #             "/etc/timezone": {
    #                 "bind": "/etc/timezone",
    #                 "mode": "ro",
    #             },
    #             "/etc/localtime": {
    #                 "bind": "/etc/localtime",
    #                 "mode": "ro",
    #             },
    #             "/dev": {"bind": "/dev", "mode": "rw"},
    #         },
    #         "cap_add": ["NET_ADMIN"],
    #         "devices": "/dev/net/tun:/dev/net/tun:rwm"
    #     },
    # )

    # enbcmd = [
    #     "srsenb",
    #     "--log.all_level=info",
    #     "--log.filename=/tmp/srsran_logs/enb.log", ">", "/proc/1/fd/1", "2>&1", "&",
    # ]
    # cmds[srsenb] = " ".join(enbcmd)

    # uecmd = [
    #     "srsue",
    #     "--log.all_level=info",
    #     "--log.filename=/tmp/srsran_logs/ue.log", ">", "/proc/1/fd/1", "2>&1", "&",
    # ]
    # cmds[srsue] = " ".join(uecmd)

    # for host in cmds:
    #     log.debug(f"::: Running cmd in container ({host.name}): {cmds[host]}\n")
    #     host.cmd(cmds[host])
    #     time.sleep(1)

    # for host in net.hosts:
    #     proc = subprocess.Popen(
    #         [
    #             "gnome-terminal",
    #             f"--display={os.environ['DISPLAY']}",
    #             "--disable-factory",
    #             "--",
    #             "docker",
    #             "logs",
    #             "-f",
    #             host.name,
    #         ],
    #         stdin=subprocess.DEVNULL,
    #         stdout=subprocess.DEVNULL,
    #         stderr=subprocess.DEVNULL,
    #     )
    #     log.debug(f"::: Spawning terminal with {proc.args}")


    info("*** Add controller\n")
    c0 = net.addController("c0")

    info("*** Adding switch\n")
    s1 = net.addSwitch("s1")
    #s2 = net.addSwitch("s2")

    info("*** Adding links\n")
    net.addLink(oaispgwu,  s1, bw=1000, delay="1ms", intfName1="oaispgwu-s1",  intfName2="s1-oaispgwu")
    #net.addLink(srsue,  s1, bw=1000, delay="1ms", intfName1="srsue-s1",  intfName2="s1-srsue")
    #net.addLink(srsenb, s2, bw=1000, delay="1ms", intfName1="srsenb-s2", intfName2="s2-srsenb")
    
    info("\n*** Starting network\n")
    c0.start()
    s1.start([c0])
    #s2.start([c0])
    #s1.cmd("ip link add s1-gre1 type gretap local 192.168.56.101 remote 192.168.56.102 ttl 64")
    #s1.cmd("ip link set s1-gre1 up")
    #Intf("s1-gre1", node=s1)

    #s2.cmd("ip link add s2-gre1 type gretap local 192.168.56.101 remote 192.168.56.102 ttl 64")
    #s2.cmd("ip link set s2-gre1 up")
    #Intf("s2-gre1", node=s2)

    info("\n*** Running CLI\n")
    net.start()

if not AUTOTEST_MODE:
    CLI(net)
    #s1.cmd("ip link del dev s1-gre1")
    #s2.cmd("ip link del dev s2-gre1")
    net.stop()