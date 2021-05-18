import intent
import chatbot
import sys

sys.path.insert(1, 'connection/tcp')

import client


def define_intents():
    saludos = intent.Intent(
        "saludos", ["hola", " buenos dias", "buenas", "saludos", "cordial saludo"], ["hola, en que le puedo ayudar?"])

    despedidas = intent.Intent(
        "despedida", ["adios", "hasta luego", "chao", "hasta pronto"], ["adios", "hasta luego", "chao", "hasta pronto"])

    sintomas = intent.Intent(
        "sintomas", ["tengo fiebre", "tengo dolor de cabeza", "tengo gripa", "tengo covid"], ["que otros sintomas tiene?"])

    return [saludos, sintomas, despedidas]


intents = define_intents()
chatbot = chatbot.Chatbot(intents)

c = client.Client()

print("Chatbot...")
while True:
    text = input()
    print(chatbot.answer(text))
