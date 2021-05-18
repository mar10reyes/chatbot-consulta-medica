# Client program
from socket import *

# Set the socket parameters
host = "localhost"
port = 514
buf = 1024
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)

def_msg = ("===Ingresa tu mensaje para el servidor===");
print ("\n"),def_msg

# Send messages
while (1):
       data = raw_input('>> ')
       if not data:
           break
       else:
           if(UDPSock.sendto(data,addr)):
               print ("Enviando mensaje '"),data,("'.....")
