"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
import requests
import ipdb
import config
from responder import generate_response

app = Flask(__name__)
TOKEN = config.FACEBOOK_TOKEN
bot = Bot(TOKEN)

@app.route("/webhook", methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if (request.args.get("hub.verify_token") == config.VERIFY_TOKEN):
                return request.args.get("hub.challenge")
    if request.method == 'POST':
        output = request.json
        event = output['entry'][0]['messaging']
        for x in event:
            if (x.get('message') and x['message'].get('text')):
                print("got a message")
                message = generate_response(x['message']['text'])
                recipient_id = x['sender']['id']
                bot.send_text_message(recipient_id, message)
            else:
                pass
        return "success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
