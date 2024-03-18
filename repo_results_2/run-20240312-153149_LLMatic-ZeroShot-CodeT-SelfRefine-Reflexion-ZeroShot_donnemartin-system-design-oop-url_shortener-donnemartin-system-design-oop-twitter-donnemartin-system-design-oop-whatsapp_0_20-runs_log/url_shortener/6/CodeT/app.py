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
	custom_alias = data.get('alias')
	username = data.get('username')
	expiration = data.get('expiration')

	# Validate URL
	# For simplicity, we'll just check if it starts with http
	if not original_url.startswith('http'):
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if custom alias is available
	if custom_alias and custom_alias in urls:
		return jsonify({'error': 'Alias already in use'}), 400

	# Generate random alias if not provided
	if not custom_alias:
		custom_alias = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

	# Create URL object
	url = URL(original=original_url, shortened=custom_alias, user=username, clicks=0, click_data=[], expiration=expiration)
	urls[custom_alias] = url

	# Add URL to user's list
	if username:
		users[username].urls.append(url)

	return jsonify({'shortened_url': custom_alias}), 200

@app.route('/<alias>', methods=['GET'])
def redirect_url(alias):
	url = urls.get(alias)

	# Check if URL exists
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expiration and datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 410

	# Increment click count and add click data
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.now().isoformat()})

	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')

	# Check if user exists
	if not username or username not in users:
		return jsonify({'error': 'User not found'}), 404

	# Get user's URLs
	user_urls = users[username].urls

	# Prepare analytics data
	analytics = []
	for url in user_urls:
		analytics.append({
			'original': url.original,
			'shortened': url.shortened,
			'clicks': url.clicks,
			'click_data': url.click_data
		})

	return jsonify(analytics), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is available
	if username in users:
		return jsonify({'error': 'Username already taken'}), 400

	# Create user object
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
