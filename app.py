#!/usr/bin/python
__author__ = 'Michael Rosata mrosata1984@gmail.com'
__package__ = 'catalog-full-stack'

# Python Library imports
import os
# External Modules
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template


# Create the Flask app
app = Flask(__name__)
# Pull our custom config settings into Flask app config object
app.config.from_object(os.environ['APP_SETTINGS'])
# Get reference to the database that we will use. (The database url is stored
# inside the app.config object now, I had created it as an Environment Var.
db = SQLAlchemy(app)


# Setup routes
@app.route('/')
def mainApp():
    conf = os.environ['APP_SETTINGS']
    return render_template('_index_.html', pythonmsg=conf)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
