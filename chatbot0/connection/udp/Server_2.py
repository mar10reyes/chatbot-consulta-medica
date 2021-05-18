# Server program
# UDP VERSION


from socket import *

# Set the socket parameters
host = "localhost"
port = 514
buf = 1024
addr = (host,port)

# Create socket and bind to address
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)

# Receive messages
while 1:
       data,addr = UDPSock.recvfrom(buf)
       if not data:
           print ("Cliente se ha salido!")
           break
       else:
           print ("\nMensaje recibido '"), data,("'")

# Close socket
UDPSock.close()
