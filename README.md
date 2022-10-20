# ARP-spoofer
ARP Spoofer for MITM, send ARP Packets(false packets) to the victim on the network

## Usage
- `pip3 install -r requirements.txt`

output:

```
usage: spoofer.py [-h] [-T TARGET] [-H HOST] [-v]

ARP spoof script

options:
  -h, --help            show this help message and exit
  -T TARGET, --target TARGET
                        Victim IP Address to ARP poison
  -H HOST, --host HOST  Host IP Address, the host you wish to intercept packets for (usually the gateway)
  -v, --verbose         verbosity, default is True (simple message each second)
```

For instance, if you want to spoof <b>192.168.1.5</b> ang gateway <b>192.168.1.1</b>

```shell
python3 spoof.py -T 192.168.1.5 -H 192.168.1.1 --verbose
```
