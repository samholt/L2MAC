from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import hashlib

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	original_url: str
	short_url: str
	expiration_date: datetime
	clicks: int

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[username] = User(username, password, {})
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	username = data.get('username')
	expiration_date = data.get('expiration_date')
	short_url = hashlib.sha1(original_url.encode()).hexdigest()[:10]
	url = URL(original_url, short_url, expiration_date, 0)
	urls[short_url] = url
	if username:
		users[username].urls[short_url] = url
	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url or (url.expiration_date and datetime.now() > url.expiration_date):
		return jsonify({'message': 'URL not found or expired'}), 404
	url.clicks += 1
	return redirect(url.original_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
