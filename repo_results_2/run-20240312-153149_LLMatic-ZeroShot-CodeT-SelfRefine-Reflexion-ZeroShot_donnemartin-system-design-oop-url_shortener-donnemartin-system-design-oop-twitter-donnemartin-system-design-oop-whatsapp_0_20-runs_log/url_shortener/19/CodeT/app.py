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
	click_data: list
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
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	user = data.get('user')
	expiration = data.get('expiration')
	new_url = URL(original_url, short_url, user, 0, [], expiration)
	urls[short_url] = new_url
	if user:
		users[user].urls.append(new_url)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		url.clicks += 1
		url.click_data.append({'time': datetime.now().isoformat()})
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	new_user = User(username, password, [])
	users[username] = new_user
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>/urls', methods=['GET'])
def get_user_urls(username):
	user = users.get(username)
	if user:
		return jsonify({'urls': [url.short for url in user.urls]}), 200
	else:
		return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
