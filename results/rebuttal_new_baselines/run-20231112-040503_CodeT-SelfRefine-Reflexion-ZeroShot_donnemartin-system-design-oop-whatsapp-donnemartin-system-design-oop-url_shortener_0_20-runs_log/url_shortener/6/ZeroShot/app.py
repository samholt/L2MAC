from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
import datetime
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
	expiration: datetime.datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	user = data.get('user')
	expiration = data.get('expiration')
	if expiration:
		expiration = datetime.datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S')
	url = URL(original=original_url, short=short_url, user=user, clicks=0, click_data=[], expiration=expiration)
	urls[short_url] = url
	if user:
		users[user].urls.append(url)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url or (url.expiration and url.expiration < datetime.datetime.now()):
		return jsonify({'error': 'URL not found or expired'}), 404
	url.clicks += 1
	url.click_data.append({'time': datetime.datetime.now().isoformat()})
	return redirect(url.original, code=302)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = User(username=username, password=password, urls=[])
	users[username] = user
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	return jsonify({'username': user.username, 'urls': [url.short for url in user.urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
