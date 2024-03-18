from flask import Flask, request, redirect
from dataclasses import dataclass
import requests
from geolite2 import geolite2
from datetime import datetime
import string
import random

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
	expiration_date: datetime

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if username in users:
		return {'message': 'Username already exists'}, 400
	users[username] = User(username, password, {})
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if username not in users or users[username].password != password:
		return {'message': 'Invalid username or password'}, 400
	return {'message': 'Logged in successfully'}, 200

@app.route('/shorten', methods=['POST'])
def shorten():
	username = request.json.get('username')
	original_url = request.json.get('url')
	short_url = request.json.get('short_url')
	expiration_date = request.json.get('expiration_date')
	if not short_url:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	if short_url in urls:
		return {'message': 'Short URL already exists'}, 400
	urls[short_url] = URL(original_url, short_url, [], expiration_date)
	users[username].urls[short_url] = urls[short_url]
	return {'message': 'URL shortened successfully', 'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url not in urls:
		return {'message': 'URL not found'}, 404
	url = urls[short_url]
	if datetime.now() > url.expiration_date:
		return {'message': 'URL expired'}, 400
	url.clicks.append((datetime.now(), request.remote_addr))
	return redirect(url.original_url, code=302)

@app.route('/analytics', methods=['GET'])
def analytics():
	username = request.json.get('username')
	short_url = request.json.get('short_url')
	if username not in users or short_url not in users[username].urls:
		return {'message': 'URL not found'}, 404
	url = users[username].urls[short_url]
	reader = geolite2.reader()
	clicks = [{'time': click[0], 'location': reader.get(click[1])['country']['iso_code']} for click in url.clicks]
	geolite2.close()
	return {'clicks': clicks}, 200

if __name__ == '__main__':
	app.run(debug=True)
