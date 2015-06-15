#!/usr/bin/python
__author__ = 'Michael Rosata mrosata1984@gmail.com'
__package__ = ''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/app/')
def mainApp():
    return render_template('_index_.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
