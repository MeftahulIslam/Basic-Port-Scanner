# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 01:02:28 2021

@author: mefta
"""

import socket
import sys

def show_help():
    print("multiple ip format: python3 port_scanner.py 127.0.0.1,127.0.0.2 [no. of ports (1-65535)")
    print("single ip format: python3 port_scanner.py 127.0.0.1 [no. of ports (1-65535)")
    
def scan(ip, ports):
    for port in range(1,ports):
        port_scanner(ip,port)
    
def port_scanner(ip, port):
    try:
        connection = socket.socket()
        connection.connect((ip,port))
        print(f'[+] Port {port} open')
    except:
        print("[-]")
    
def cmd_read():
    if sys.argv[1] == "-h":
         show_help()
    else:   
        try:
            ip_adds = sys.argv[1]
            ports = int(sys.argv[2])
        except IndexError:
            print("Please follow the correct syntax. For help use '-h'")
        except Exception as e:
            print(f"{e}")
        
        if ',' in ip_adds:
            for ip in ip_adds.split(','):
                print (f"/n [*] Scanning {ip}.....")
                scan(ip.strip(' '), ports)
        else:
            print(f'\n [*] Scanning {ip_adds}.....')
            scan(ip_adds.strip(' '), ports)
        
        
cmd_read()