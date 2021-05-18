import sys
import os
import json
from flask import Flask
from flask import request
import text_translator

sys.path.insert(1, 'chatbot')
import init_chatbot

app = Flask(__name__)

@app.route('/api/chatbot/', methods=['GET'])
def chatbot():
    #get the message from http parmeters
    message = request.args.get('message')
    
    #instantiate the chatbot
    chatbot = init_chatbot.start_chatbot()
    
    #translate user request
    translated_message = text_translator.translate_text(message, 'auto', 'es')
    str_translated_message = json.loads(translated_message)['translatedText']

    #get rid of punctuation signs
    str_translated_message = str_translated_message.replace('.', '')
    str_translated_message = str_translated_message.lower()
    
    #if the translated word is the same as the original is cause was already in spanish
    if str_translated_message == message:
        #if the message is already in spanish we dont need to translate the response
        response = chatbot.handle(str_translated_message)
    else:
        #if not, we translate back to english
        response = chatbot.handle(str_translated_message)
        translated_back_message = text_translator.translate_text(response, 'es', 'en')
        str_translated_back_message = json.loads(translated_back_message)['translatedText']
        response = str_translated_back_message
    
    return json.dumps({
                'answer ':response
            })


if __name__ == '__main__':
    app.run(port=1515, debug=True)