#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def say_hello():
    res = 'Hello World'
    return str(res)


# allows the app to run with a simple python main.py
if __name__ == '__main__':
    app.run()
