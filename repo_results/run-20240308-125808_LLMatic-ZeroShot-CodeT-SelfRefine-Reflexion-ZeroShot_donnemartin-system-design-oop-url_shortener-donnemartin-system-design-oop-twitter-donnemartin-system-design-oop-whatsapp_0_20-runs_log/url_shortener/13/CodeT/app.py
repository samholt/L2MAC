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
	url = URL(original=original_url, short=short_url, user=username, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S') if expiration else None)
	urls[short_url] = url

	# If user is provided, add URL to user's list of URLs
	if username:
		if username in users:
			users[username].urls.append(url)
		else:
			return jsonify({'error': 'User not found'}), 400

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	# Get URL from database
	url = urls.get(short_url)

	# If URL is not found or has expired, return an error
	if not url or (url.expiration and url.expiration < datetime.now()):
		return jsonify({'error': 'URL not found or has expired'}), 404

	# Increment click count and add click data
	url.clicks += 1
	url.click_data.append({'time': datetime.now().isoformat(), 'location': request.remote_addr})

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')

	# If username is provided, get analytics for that user's URLs
	if username:
		if username in users:
			user_urls = users[username].urls
			return jsonify({'urls': [{
				'original': url.original,
				'short': url.short,
				'clicks': url.clicks,
				'click_data': url.click_data
			} for url in user_urls]}), 200
		else:
			return jsonify({'error': 'User not found'}), 400

	# If no username is provided, get analytics for all URLs
	return jsonify({'urls': [{
		'original': url.original,
		'short': url.short,
		'clicks': url.clicks,
		'click_data': url.click_data
	} for url in urls.values()]}), 200

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already in use
	if username in users:
		return jsonify({'error': 'Username is already in use'}), 400

	# Create user and store in database
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User created successfully'}), 200

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
	# Get user from database
	user = users.get(username)

	# If user is not found, return an error
	if not user:
		return jsonify({'error': 'User not found'}), 404

	# Return user data
	return jsonify({'username': user.username, 'urls': [{'original': url.original, 'short': url.short} for url in user.urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
