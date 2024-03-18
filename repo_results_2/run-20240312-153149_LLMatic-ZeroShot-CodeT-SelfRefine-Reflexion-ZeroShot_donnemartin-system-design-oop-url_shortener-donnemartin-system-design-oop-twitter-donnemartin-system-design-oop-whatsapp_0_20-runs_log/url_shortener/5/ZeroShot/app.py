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
	if not original_url:
		return jsonify({'error': 'URL is required'}), 400

	# Generate short URL
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom_short:
		short_url = custom_short

	# Create URL object
	url = URL(original=original_url, short=short_url, user=username, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S'))

	# Save URL to database
	urls[short_url] = url

	# Add URL to user's list
	if username:
		users[username].urls.append(url)

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Increment click count
	url.clicks += 1
	url.click_data.append({'click_time': datetime.now().isoformat()})

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')
	if not username:
		return jsonify({'error': 'Username is required'}), 400

	user = users.get(username)
	if not user:
		return jsonify({'error': 'User not found'}), 404

	# Get user's URLs and their analytics
	user_urls = [{'original': url.original, 'short': url.short, 'clicks': url.clicks, 'click_data': url.click_data} for url in user.urls]

	return jsonify({'urls': user_urls}), 200

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Validate input
	if not username or not password:
		return jsonify({'error': 'Username and password are required'}), 400

	# Create user object
	user = User(username=username, password=password, urls=[])

	# Save user to database
	users[username] = user

	return jsonify({'message': 'User created'}), 201

if __name__ == '__main__':
	app.run(debug=True)
