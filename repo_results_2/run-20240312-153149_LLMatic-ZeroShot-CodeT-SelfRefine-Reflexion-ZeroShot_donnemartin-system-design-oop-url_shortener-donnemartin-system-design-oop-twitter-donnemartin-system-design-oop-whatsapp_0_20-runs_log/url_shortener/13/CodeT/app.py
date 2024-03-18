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
	clicks: []
	expiration: datetime

@dataclass
class User:
	username: str
	password: str
	urls: []

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	custom_short = data.get('custom')
	username = data.get('username')
	expiration = data.get('expiration')

	# Validate URL
	# TODO: Add actual URL validation

	# Generate short URL
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom_short:
		short_url = custom_short

	# Create URL object
	url = URL(original=original_url, short=short_url, user=username, clicks=[], expiration=expiration)
	urls[short_url] = url

	# Add URL to user's list
	if username:
		users[username].urls.append(url)

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		url.clicks.append(datetime.now())
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	username = data.get('username')

	if username:
		user_urls = users[username].urls
		analytics = [{'original': url.original, 'short': url.short, 'clicks': len(url.clicks)} for url in user_urls]
		return jsonify(analytics), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Create user object
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
