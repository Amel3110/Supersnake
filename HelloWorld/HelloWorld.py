#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
application = Flask(__name__)

@application.route("/")
def HelloWorld():
    return "Hello World!"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
