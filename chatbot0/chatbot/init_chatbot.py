import intent
import chatbot
import sys

#instantiate chatbot
def define_intents():
    saludos = intent.Intent(
        "saludos", ["hola", " buenos dias", "buenas", "saludos", "cordial saludo"], ["hola, en que le puedo ayudar?"])

    despedidas = intent.Intent(
        "despedida", ["adios", "hasta luego", "chao", "hasta pronto"], ["adios", "hasta luego", "chao", "hasta pronto"])

    sintomas = intent.Intent(
        "sintomas", ["tengo fiebre", "tengo dolor de cabeza", "tengo gripa", "tengo covid"], ["que otros sintomas tiene?"])


    return [saludos, sintomas, despedidas]

def start_chatbot():
    print('init_chatbot')
    intents = define_intents()
    return chatbot.Chatbot(intents)