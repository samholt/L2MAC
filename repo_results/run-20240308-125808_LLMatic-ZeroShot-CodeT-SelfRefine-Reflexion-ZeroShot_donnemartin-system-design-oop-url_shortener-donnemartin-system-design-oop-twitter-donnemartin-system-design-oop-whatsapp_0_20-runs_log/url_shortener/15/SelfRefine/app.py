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
	short: str
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
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	user = data.get('user')
	expires_at = datetime.strptime(data.get('expires_at'), '%Y-%m-%dT%H:%M:%S')
	url = URL(original_url, short_url, user, 0, datetime.now(), expires_at)
	urls[short_url] = url
	if user:
		if user in users:
			users[user].urls.append(url)
		else:
			return jsonify({'error': 'User not found'}), 404
	return jsonify({'short_url': short_url}), 201

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
	user = User(username, password, [])
	users[username] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if user:
		return jsonify({'username': user.username, 'urls': [url.short for url in user.urls]}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)