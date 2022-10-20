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

        