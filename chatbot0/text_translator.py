
import requests

def translate_text(message, source, target):

    url = "https://libretranslate.com/translate"

    headers = { "Content-Type": "application/json" }

    body = {
            'q': message,
            'source': "auto",
            'target': "es"
        }

    response = requests.request("POST", url, json={'q': message,'source': source,'target': target}, headers=headers)
    return response.text
