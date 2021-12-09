#!/usr/bin/env python3
# Displays all SDLC data forwarded from the EM_HDLC
# Refer to Table 3.1 from NEMA TS2 Traffic Controller Assemblies with NTCIP Requirements
import socket

#Set forward IP and port in EM_HDLC web interface
# The forward IP is the IP running this
EM_HDLC_FORWARD_PORT = 10002

print("Listening on port: %s" % EM_HDLC_FORWARD_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', EM_HDLC_FORWARD_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("From " + str(addr[0]) + " port " + str(addr[1]) + " received message (HEX): %s" % data.hex())\

