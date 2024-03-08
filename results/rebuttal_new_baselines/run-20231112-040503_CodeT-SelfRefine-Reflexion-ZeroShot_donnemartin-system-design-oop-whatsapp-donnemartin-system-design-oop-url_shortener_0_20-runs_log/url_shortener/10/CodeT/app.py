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
	custom = data.get('custom')
	expiration = data.get('expiration')

	# Validate URL
	# For simplicity, we'll just check if it starts with http
	if not original_url.startswith('http'):
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate shortened URL
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom:
		shortened_url = custom

	# Create URL object
	url = URL(original_url, shortened_url, user, 0, [], expiration)

	# Add to database
	urls[shortened_url] = url

	return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = urls.get(shortened_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	shortened_url = data.get('url')
	user = data.get('user')

	url = urls.get(shortened_url)
	if not url or url.user != user:
		return jsonify({'error': 'URL not found'}), 404

	# Return analytics data
	return jsonify({'clicks': url.clicks, 'click_data': url.click_data}), 200

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Create user object
	user = User(username, password, [])

	# Add to database
	users[username] = user

	return jsonify({'message': 'User created'}), 200

@app.route('/user/urls', methods=['GET'])
def get_user_urls():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	user = users.get(username)
	if not user or user.password != password:
		return jsonify({'error': 'User not found'}), 404

	# Return user's URLs
	return jsonify({'urls': [url.shortened for url in user.urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
