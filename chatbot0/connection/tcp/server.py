import socket
import threading


class Server():
    def __init__(self, request_handler):

        # Connection Data
        self.host = '127.0.0.1'
        self.port = 55555

        # Starting Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        # Lists For Clients and Their Nicknames
        self.clients = []
        self.nicknames = []

        # object for request handling
        self.request_handler = request_handler

    
    #def send_message(self, client, response):
        #client.send(response)
    
    # Handling Messages From Clients
    def client_request(self, client):
        while True:
            try:
                # Broadcasting Messages
                #print("before message")
                message = client.recv(1024).decode('ascii')
                print("Request: "+message)
                response = self.request_handler.handle(message)
                print('returned form chatbot: '+str(response))
                client.send(str(response).encode('ascii'))

            except:
                # Removing And Closing Clients
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                break

    def receive(self):
        while True:
            # Accept Connection
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))

            # Request And Store Nickname
            #client.send('NICK'.encode('ascii'))
            #nickname = client.recv(1024).decode('ascii')
            self.nicknames.append("user")
            self.clients.append(client)

            # Print And Broadcast Nickname
            #print("Nickname is {}".format(nickname))
            #client.send('Connected to server!'.encode('ascii'))

            #client.send("hola-hardcoded".encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=self.client_request, args=(client,))
            thread.start()
