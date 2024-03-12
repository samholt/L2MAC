from flask import Flask, request, redirect
from dataclasses import dataclass
import requests
from datetime import datetime
from geolite2 import geolite2

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	original_url: str
	short_url: str
	clicks: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# TODO
	pass

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
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

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	# TODO
	pass

if __name__ == '__main__':
	app.run(debug=True)
