import socket
import threading
import asyncio
import time


class Client():

    def __init__(self):

        # Choosing Nickname
        self.nickname = "user"

        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 55555))

    # Listening to Server and Sending Nickname
    def receive(self):
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                #message = asyncio.create_task(self.client.recv(1024).decode('ascii'))
                message = self.client.recv(1024).decode('ascii')
                #message = "hola, como estas? (-----)"
                print(message)

                #message = self.client.recv(1024).decode('ascii')

                return message
            except:
                # Close Connection When Error
                print("An error occured!")
                self.client.close()
                break

    # Sending Messages To Server

    def write(self, message):
        #while True:
        #message = '{}: {}'.format(self.nickname, input(''))
        self.client.send(message.encode('ascii'))

        #wait for the response async
        #loop = asyncio.get_event_loop()
        #print("loop: "+str(loop))
        #response = loop.run_until_complete(self.receive())
        #print("res: "+str(response))
        #loop.close()
        #print("loop: "+str(loop))
        
        response = self.receive()
        return response


    def chat(self):
        # Starting Threads For Listening And Writing
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()
