#!/usr/bin/python
__author__ = 'Michael Rosata mrosata1984@gmail.com'
__package__ = 'catalog-full-stack'

# Python Module Imports.
import os

# Scripts to migrate Flask SQLAlchemy to the cloud.
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# Local imports.
from app import app, db

# Store our environment variables into Flask App config object.
app.config.from_object(os.environ['APP_SETTINGS'])

# Give migrate our app and db information.
migrate = Migrate(app, db)

# Set command `db` as command to run postgres migrations from the command-line.
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
