from flask import Flask, request, redirect, jsonify
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
	clicks: list
	expiration: datetime

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
	expiration = data.get('expiration')
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[shortened_url] = URL(original_url, shortened_url, user, [], expiration)
	if user:
		users[user].urls.append(shortened_url)
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		url.clicks.append(datetime.now())
		return redirect(url.original, code=302)
	else:
		return 'URL not found or expired', 404

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	users[username] = User(username, password, [])
	return 'User created', 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if user:
		return jsonify({'username': user.username, 'urls': user.urls}), 200
	else:
		return 'User not found', 404

@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
	user = users.get(username)
	if user:
		for url in user.urls:
			del urls[url]
		del users[username]
		return 'User deleted', 200
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
