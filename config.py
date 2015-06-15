#!/usr/bin/python
__author__ = 'Michael Rosata mrosata1984@gmail.com'

# Most of this class comes pretty much from an idea in a tutorial, so I'm not
# 100% sure that all instances will remain useful or used. At the moment I shut
# down even having a staging app due to the fact that this is my first Heroku
# app so I might focus more on learning, then a staging repo and app can be
# created bippity boppity boop anyways.

# To use this file, I added a line to ~/Envs/postactivate
# export APP_SETINGS="config.DevelopmentConfig"

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'Z@b77Dha3b3b@dii3ou;e5123nd9xsa'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True