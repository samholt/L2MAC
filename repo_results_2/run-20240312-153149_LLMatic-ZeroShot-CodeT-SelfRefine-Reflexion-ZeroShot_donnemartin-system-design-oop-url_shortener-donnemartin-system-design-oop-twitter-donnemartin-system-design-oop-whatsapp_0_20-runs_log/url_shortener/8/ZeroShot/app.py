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
	shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	if custom:
		shortened_url = custom

	# Create URL object and store in database
	url = URL(original_url, shortened_url, user, 0, [], expiration)
	urls[shortened_url] = url

	# If user is provided, add URL to user's list
	if user:
		users[user].urls.append(url)

	return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	# Check if URL exists
	if shortened_url not in urls:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL is expired
	if urls[shortened_url].expiration and urls[shortened_url].expiration < datetime.now():
		return jsonify({'error': 'URL expired'}), 410

	# Increment click count and add click data
	urls[shortened_url].clicks += 1
	urls[shortened_url].click_data.append({'time': datetime.now().isoformat()})

	# Redirect to original URL
	return redirect(urls[shortened_url].original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# If user is provided, return analytics for user's URLs
	if user:
		return jsonify({'urls': [url.__dict__ for url in users[user].urls]}), 200

	# Otherwise, return analytics for all URLs
	return jsonify({'urls': [url.__dict__ for url in urls.values()]}), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is taken
	if username in users:
		return jsonify({'error': 'Username taken'}), 400

	# Create user and store in database
	user = User(username, password, [])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	# For simplicity, we'll just return all URLs and users
	return jsonify({'urls': [url.__dict__ for url in urls.values()], 'users': [user.__dict__ for user in users.values()]}), 200

if __name__ == '__main__':
	app.run(debug=True)
