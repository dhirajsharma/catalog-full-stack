#!/usr/bin/python
__author__ = 'Michael Rosata mrosata1984@gmail.com'
__package__ = 'catalog-full-stack'

from app import db
from sqlalchemy.dialects.postgresql import JSON


# Use this as a basic template for a Table class. It has its own __init__
# method to use to add a row. This uses JSON data type. It also has a __repr__
# method for printing to the console.
class Testing(db.Model):
    __tablename__ = 'testing'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64))
    result = db.Column(JSON)

    def __init__(self, url, result):
        self.url = url
        self.result = result

    def __repr__(self):
        return '<id {}>'.format(self.id)

