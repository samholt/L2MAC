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
	original_url = data['url']
	user = data.get('user')
	expiration = data.get('expiration')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original=original_url, short=short_url, user=user, clicks=0, click_data=[], expiration=expiration)
	urls[short_url] = url
	if user:
		users[user].urls.append(url)
	return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		url.clicks += 1
		url.click_data.append({'click_time': datetime.now().isoformat()})
		return redirect(url.original, code=302)
	else:
		return 'URL not found or expired', 404

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username=username, password=password, urls=[])
	users[username] = user
	return 'User created', 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if user:
		return jsonify({'username': user.username, 'urls': [url.short for url in user.urls]})
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
