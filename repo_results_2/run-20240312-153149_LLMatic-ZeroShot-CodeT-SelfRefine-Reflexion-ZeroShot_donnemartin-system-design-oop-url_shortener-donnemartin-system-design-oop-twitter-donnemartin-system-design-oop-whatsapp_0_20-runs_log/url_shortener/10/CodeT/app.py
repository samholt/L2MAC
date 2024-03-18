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

	# Check if custom short URL is available
	if custom_short and custom_short in urls:
		return jsonify({'error': 'Custom short URL is already in use'}), 400

	# Generate a random short URL if no custom one is provided
	short_url = custom_short or ''.join(random.choices(string.ascii_letters + string.digits, k=5))

	# Create URL object and store in database
	url = URL(original=original_url, short=short_url, user=username, clicks=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S') if expiration else None)
	urls[short_url] = url

	# Add URL to user's list of URLs
	if username:
		users[username].urls.append(url)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	url = urls.get(short_url)

	# Check if URL exists and has not expired
	if not url or (url.expiration and url.expiration < datetime.now()):
		return jsonify({'error': 'URL not found or expired'}), 404

	# Record click
	url.clicks.append({'timestamp': datetime.now().isoformat()})

	return redirect(url.original, code=302)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already taken
	if username in users:
		return jsonify({'error': 'Username is already taken'}), 400

	# Create user and store in database
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User created successfully'}), 200

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)

	# Check if user exists
	if not user:
		return jsonify({'error': 'User not found'}), 404

	# Return user's URLs
	return jsonify({'urls': [url.short for url in user.urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
