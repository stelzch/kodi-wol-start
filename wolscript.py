#!/usr/bin/python3
import sys
from socket import *

HOST = "0.0.0.0"
INTERFACE = "eth0"
WAKE_ON_LAN_PORT = 9

# Returns MAC address of interface as byte array
def get_mac(iface):
    with open("/sys/class/net/{}/address".format(iface)) as f:
        string = f.readline() \
                    .strip()  \
                    .split(':')
        hexarr = map(lambda v: int(v, 16), string)
        return bytes(hexarr)

MAC = get_mac(INTERFACE)


s = socket(AF_INET, SOCK_DGRAM) # UDP
s.bind((HOST, WAKE_ON_LAN_PORT))


while True:
    data = s.recv(1024)

    if len(data) == 102 \
            and data[:6] == bytes([0xff]) * 6 \
            and data[6:] == MAC * 16:
        sys.exit(0)

sys.exit(-1)
