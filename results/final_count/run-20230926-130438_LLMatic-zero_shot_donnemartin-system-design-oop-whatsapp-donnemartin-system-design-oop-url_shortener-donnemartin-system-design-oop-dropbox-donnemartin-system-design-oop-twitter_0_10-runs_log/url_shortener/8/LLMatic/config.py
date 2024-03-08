import os

class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = os.urandom(24)
