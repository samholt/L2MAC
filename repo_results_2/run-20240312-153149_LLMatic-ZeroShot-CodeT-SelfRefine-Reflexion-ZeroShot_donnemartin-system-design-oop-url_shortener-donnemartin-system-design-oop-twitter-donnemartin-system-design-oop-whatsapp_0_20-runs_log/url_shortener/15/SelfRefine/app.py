from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string
import bcrypt

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
	user = data.get('user')
	expiration = data.get('expiration')
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[shortened_url] = URL(original_url, shortened_url, user, 0, [], expiration)
	if user:
		if bcrypt.checkpw(data.get('password').encode(), users[user].password):
			users[user].urls.append(shortened_url)
			return jsonify({'shortened_url': shortened_url}), 200
		else:
			return jsonify({'error': 'Invalid password'}), 403
	else:
		return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = urls.get(shortened_url)
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
	password = bcrypt.hashpw(data.get('password').encode(), bcrypt.gensalt())
	users[username] = User(username, password, [])
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>/urls', methods=['GET'])
def get_user_urls(username):
	user = users.get(username)
	if user:
		if bcrypt.checkpw(request.args.get('password').encode(), user.password):
			return jsonify({'urls': [urls[url].original for url in user.urls]}), 200
		else:
			return jsonify({'error': 'Invalid password'}), 403
	else:
		return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
