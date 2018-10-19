#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

import json
from twilio.rest import Client

# importing the json data and setting them to variables
with open('secrets.json') as json_data:
    d = json.load(json_data)

account_sid = d['SID']
account_auth_token = d['AUTH_TOKEN']
account_number = d['TWILIO_NUMBER']

client = Client(account_sid, account_auth_token)


@app.route('/hello', methods=['GET'])
def send_message():

    message = client.messages.create(
        to="+19783405051",
        from_=account_number,
        body="Hello from Python!")

    return str(message.sid)


# allows the app to run with a simple python main.py
if __name__ == '__main__':
    app.run()
