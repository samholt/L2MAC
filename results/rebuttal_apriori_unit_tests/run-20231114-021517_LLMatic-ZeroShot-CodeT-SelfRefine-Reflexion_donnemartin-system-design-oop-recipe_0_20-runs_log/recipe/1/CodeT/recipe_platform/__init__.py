from flask import Flask
from . import models

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'
