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
	custom_short = data.get('custom')
	username = data.get('username')
	expiration = data.get('expiration')

	# Validate URL
	# For simplicity, we'll just check if it starts with http
	if not original_url.startswith('http'):
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if the URL has already been shortened
	for url in urls.values():
		if url.original == original_url:
			return jsonify({'short_url': url.short}), 200

	# Check if custom short URL is available
	if custom_short:
		if custom_short in urls:
			return jsonify({'error': 'Custom short URL is already in use'}), 400
		else:
			# If custom short URL is not in use, use it
			short_url = custom_short
	else:
		# Generate a random short URL if no custom one is provided
		short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

	# Create URL object and store it
	url = URL(original=original_url, short=short_url, user=username, clicks=[], expiration=expiration)
	urls[short_url] = url

	# If user is provided, add URL to user's list
	if username:
		if username in users:
			users[username].urls.append(url)
		else:
			return jsonify({'error': 'User not found'}), 400
	else:
		# If no user is provided, associate the URL with a default 'anonymous' user
		if 'anonymous' not in users:
			users['anonymous'] = User(username='anonymous', password='', urls=[])
		users['anonymous'].urls.append(url)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	# Check if URL exists
	if short_url not in urls:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if urls[short_url].expiration and urls[short_url].expiration < datetime.now():
		return jsonify({'error': 'URL has expired'}), 410

	# Redirect to original URL
	return redirect(urls[short_url].original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')

	# Check if user exists
	if username not in users:
		return jsonify({'error': 'User not found'}), 404

	# Get user's URLs and their analytics
	user_urls = users[username].urls
	analytics = [{
		'url': url.short,
		'clicks': len(url.clicks),
		'last_clicked': max(url.clicks) if url.clicks else None
	} for url in user_urls]

	return jsonify(analytics), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already taken
	if username in users:
		return jsonify({'error': 'Username is already taken'}), 400

	# Create user and store it
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
