from flask import Flask, request, redirect
from dataclasses import dataclass
import requests
from datetime import datetime
from geolite2 import geolite2

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class URL:
	original: str
	shortened: str
	clicks: list

@dataclass
class User:
	username: str
	password: str
	urls: list

@dataclass
class Admin(User):
	pass

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# TODO
	pass

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	# TODO
	pass

@app.route('/analytics', methods=['GET'])
def get_analytics():
	# TODO
	pass

@app.route('/user', methods=['POST'])
def create_user():
	# TODO
	pass

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(username):
	# TODO
	pass

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	# TODO
	pass

@app.route('/expire', methods=['POST'])
def set_expiration():
	# TODO
	pass

if __name__ == '__main__':
	app.run(debug=True)
