#!/usr/bin/env python3

import socket
import time

#Set the IP address and port of the machine running this script
# in the EM_HDLC web interface system tab command IP/port.
EM_HDLC_IP = "192.168.1.124"
EM_HDLC_PORT = 10001

DISCOVER = b'LXBIU\x01\x01\x00'
# Sets timeout to five seconds
SET_TIMEOUT = b'LXBIU\x01\x02\x01\x05'
ENABLE_MASK = b'LXBIU\x01\x03\x01\x01'
UPDATE_BIU1_CALL_DATA = b'LXBIU\x01\x0a\x27\x08\x83\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print("EM HDLC IP: %s" % EM_HDLC_IP)
print("EM_HDLC port: %s" % EM_HDLC_PORT)

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM) # UDP
sock.bind(('0.0.0.0', EM_HDLC_PORT))

def em_command (command):
    """Send a command and wait for a response"""
    sock.sendto(command, (EM_HDLC_IP, EM_HDLC_PORT))
    sock.settimeout(2)
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        if len(data) is not None:
            print("received command response: %s" % data.hex())
    except:
        print("timeout")

# Check configuration
em_command(DISCOVER)

while True:
    em_command(SET_TIMEOUT)
    em_command(ENABLE_MASK)
    em_command(UPDATE_BIU1_CALL_DATA)
    time.sleep(0.5)


