#!/usr/bin/python
__author__ = 'Michael Rosata mrosata1984@gmail.com'
__package__ = ''

import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def mainApp():
    conf = os.environ['APP_SETTINGS']
    return render_template('_index_.html', pythonmsg=conf)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
