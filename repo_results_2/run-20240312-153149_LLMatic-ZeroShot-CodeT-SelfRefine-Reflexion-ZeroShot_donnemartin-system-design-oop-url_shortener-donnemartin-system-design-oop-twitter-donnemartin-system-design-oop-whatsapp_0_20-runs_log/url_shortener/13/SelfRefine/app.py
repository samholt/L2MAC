from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string
from urllib.parse import urlparse

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
	custom_short = data.get('custom')
	username = data.get('username')
	expiration = data.get('expiration')

	# Validate URL
	try:
		result = urlparse(original_url)
		if all([result.scheme, result.netloc]):
			pass
		else:
			return jsonify({'error': 'Invalid URL'}), 400
	except ValueError:
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom_short:
		if custom_short in urls:
			return jsonify({'error': 'Custom short URL already in use'}), 400
		short_url = custom_short

	# Create URL object
	url = URL(original=original_url, short=short_url, user=username, clicks=0, click_data=[], expiration=expiration)

	# Add URL to database
	urls[short_url] = url

	# Add URL to user's list
	if username:
		users[username].urls.append(url)

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		# Increment click count
		url.clicks += 1
		# TODO: Add click data
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')
	if username:
		user_urls = users[username].urls
		return jsonify([url.__dict__ for url in user_urls]), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Create user object
	user = User(username=username, password=password, urls=[])

	# Add user to database
	users[username] = user

	return jsonify({'message': 'User created'}), 201

if __name__ == '__main__':
	app.run(debug=True)
