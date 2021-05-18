import sys
import json

sys.path.insert(1, 'connection/rmi')
sys.path.insert(1, 'connection/tcp')

import rmi_client
from request_handler import RequestHandler

class Chatbot(RequestHandler):
    def __init__(self, intents):
        self.intents = intents

    def identify_intent(self, text):
        for intent in self.intents:
            for pattern in intent.patterns:
                if text == pattern:
                    return intent

        return None

    def answer(self, text):
        intent = self.identify_intent(text)

        if intent:
            return intent.response()
        return "No entiendo lo que quires decir"

    def get_symptoms(self, request):

        symptoms = []

        request = request.replace("tengo ","")
        print("before replacing y")
        request = request.replace(' y ',',')
        print("replaced y")
        request = request.replace(' ','')
        print("replaced spaces")
        
        symptoms = request.split(',')
        
        return symptoms
    
    def call_diagnose(self, request):
        
        symptoms = self.get_symptoms(request)

        ns = Pyro4.locateNS()
        uri = ns.lookup('remote_object')

        #uri = "PYRO:obj_92a6abe21ddb4dffad3a39184497961a@localhost:64425"

        print("before client creation")
        c = rmi_client.RMIClient(uri)
        print("instantiation of client object: "+str(c))
        
        remote_object = c.connect()
        print("remote object: "+str(remote_object))

        response = remote_object.diagnose(symptoms)
        
        print("response: "+str(response['medicine']))

        if response != None:
            
            disease = str(response['name'])
            medicine = str(response['medicine'])

            if "N/A" not in medicine:
                return str("Tienes "+disease+" y para curarte debes tomar "+medicine)
            else:
                return str("Tienes "+disease+" y no hay medicinas que puedas tomar")

        return "No es claro que enfermedad tienes, te llamara una persona lo antes posible para que agendes una cita"

    def handle(self, request):
        print("handle method...")
        
        if "tengo" in request:
            return self.call_diagnose(request)
        else:
            print("tengo is not a sub string")
        
        return self.answer(request)
