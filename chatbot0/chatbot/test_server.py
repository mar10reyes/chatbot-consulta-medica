#from chatbot.intent import intent
#from chatbot.chatbot import chatbot
import intent
import chatbot
import sys

sys.path.insert(1, 'connection/tcp')

import server

s = server.Server()
s.receive()
