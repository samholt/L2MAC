from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import string

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
	clicks: int
	click_data: list
	expiration: datetime

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
def shorten():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	original_url = data['original_url']
	short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
	expiration = datetime.now() + timedelta(days=1) # URL expires after 1 day
	if 'short_url' in data:
		short_url = data['short_url']
	if short_url in urls:
		return jsonify({'message': 'Short URL already exists'}), 400
	for url in urls.values():
		if url.original_url == original_url:
			return jsonify({'message': 'URL already shortened', 'short_url': url.short_url}), 200
	urls[short_url] = URL(original_url, short_url, 0, [], expiration)
	users[username].urls[short_url] = urls[short_url]
	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	if short_url not in urls or datetime.now() > urls[short_url].expiration:
		return jsonify({'message': 'URL not found or expired'}), 404
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'timestamp': datetime.now().isoformat()})
	return redirect(urls[short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def analytics():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	user_urls = users[username].urls
	analytics_data = {url.short_url: {'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls.values()}
	return jsonify(analytics_data), 200

if __name__ == '__main__':
	app.run(debug=True)
