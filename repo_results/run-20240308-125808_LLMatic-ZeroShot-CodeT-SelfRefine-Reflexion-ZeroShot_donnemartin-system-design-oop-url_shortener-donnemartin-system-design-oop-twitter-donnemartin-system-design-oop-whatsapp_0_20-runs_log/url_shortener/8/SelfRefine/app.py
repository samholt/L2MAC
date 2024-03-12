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
	if not custom_short:
		custom_short = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

	# Create URL object and store in database
	url = URL(original=original_url, short=custom_short, user=username, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S') if expiration else None)
	urls[custom_short] = url

	# Add URL to user's list of URLs
	if username:
		users[username].urls.append(url)

	return jsonify({'short_url': custom_short}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	# Check if short URL exists
	if short_url not in urls:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if urls[short_url].expiration and urls[short_url].expiration < datetime.now():
		return jsonify({'error': 'URL has expired'}), 410

	# Increment click count and add click data
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'time': datetime.now().isoformat(), 'location': request.remote_addr})

	# Redirect to original URL
	return redirect(urls[short_url].original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')

	# Check if user exists
	if username not in users:
		return jsonify({'error': 'User not found'}), 404

	# Get analytics for all of user's URLs
	analytics = [{
		'url': url.short,
		'clicks': url.clicks,
		'click_data': url.click_data
	} for url in users[username].urls]

	return jsonify(analytics), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already taken
	if username in users:
		return jsonify({'error': 'Username is already taken'}), 400

	# Create user and store in database
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	# For simplicity, we'll assume that there's no authentication required to access the admin dashboard
	# Get all URLs and users
	all_urls = [{
		'url': url.short,
		'original': url.original,
		'user': url.user,
		'clicks': url.clicks,
		'expiration': url.expiration.isoformat() if url.expiration else None
	} for url in urls.values()]
	all_users = [{
		'username': user.username,
		'urls': [url.short for url in user.urls]
	} for user in users.values()]

	return jsonify({'urls': all_urls, 'users': all_users}), 200

if __name__ == '__main__':
	app.run(debug=True)
