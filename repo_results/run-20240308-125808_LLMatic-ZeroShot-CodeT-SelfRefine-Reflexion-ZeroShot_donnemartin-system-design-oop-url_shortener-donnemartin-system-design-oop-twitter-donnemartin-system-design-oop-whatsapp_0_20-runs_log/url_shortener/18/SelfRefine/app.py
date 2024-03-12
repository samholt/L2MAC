from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	created_at: datetime
	expires_at: datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	expires_at = data.get('expires_at')
	if not expires_at:
		expires_at = datetime.max
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url, shortened_url, user, 0, datetime.now(), expires_at)
	urls[shortened_url] = url
	if user:
		users[user].urls.append(url)
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and url.expires_at > datetime.now():
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in users:
		return jsonify({'error': 'User already exists'}), 400
	user = User(username, password, [])
	users[username] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	data = request.get_json()
	password = data.get('password')
	user = users.get(username)
	if user and user.password == password:
		return jsonify({'username': user.username, 'urls': [url.shortened for url in user.urls]}), 200
	else:
		return jsonify({'error': 'User not found or incorrect password'}), 404

@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
	data = request.get_json()
	password = data.get('password')
	user = users.get(username)
	if user and user.password == password:
		del users[username]
		return jsonify({'message': 'User deleted'}), 200
	else:
		return jsonify({'error': 'User not found or incorrect password'}), 404

if __name__ == '__main__':
	app.run(debug=True)
