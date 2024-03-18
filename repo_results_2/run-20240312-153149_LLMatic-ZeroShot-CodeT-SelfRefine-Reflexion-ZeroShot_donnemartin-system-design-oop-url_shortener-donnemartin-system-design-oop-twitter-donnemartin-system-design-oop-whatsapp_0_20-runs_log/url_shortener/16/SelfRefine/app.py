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
	url = URL(original=original_url, short=custom_short, user=username, clicks=0, click_data=[], expiration=expiration)
	urls[custom_short] = url

	# If user is provided, add URL to user's list
	if username:
		if username in users:
			users[username].urls.append(url)
		else:
			# Create user and store in database
			user = User(username=username, password='', urls=[])
			users[username] = user
			users[username].urls.append(url)

	return jsonify({'short_url': custom_short}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	# Check if URL exists
	if short_url not in urls:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL is expired
	if urls[short_url].expiration and urls[short_url].expiration < datetime.now():
		return jsonify({'error': 'URL is expired'}), 410

	# Increment click count and add click data
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'time': datetime.now().isoformat()})

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
	analytics = [{'original': url.original, 'short': url.short, 'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls]

	return jsonify(analytics), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username and password are provided
	if not username or not password:
		return jsonify({'error': 'Username and password are required'}), 400

	# Check if username is already taken
	if username in users:
		return jsonify({'error': 'Username is already taken'}), 400

	# Create user and store in database
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	# For simplicity, we'll assume that the admin is always authenticated
	all_urls = [{'original': url.original, 'short': url.short, 'user': url.user, 'clicks': url.clicks, 'click_data': url.click_data} for url in urls.values()]
	return jsonify(all_urls), 200

if __name__ == '__main__':
	app.run(debug=True)
