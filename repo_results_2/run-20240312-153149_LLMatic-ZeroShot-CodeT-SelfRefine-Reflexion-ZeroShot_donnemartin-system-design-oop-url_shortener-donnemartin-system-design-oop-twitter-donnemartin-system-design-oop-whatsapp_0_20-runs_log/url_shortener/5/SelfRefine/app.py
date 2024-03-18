from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string
import hashlib

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

	# Generate random alias if not provided
	if not custom_alias:
		custom_alias = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

	# Check if alias already exists
	if custom_alias in urls:
		return jsonify({'error': 'Alias already exists'}), 400

	# Validate expiration date
	if expiration:
		try:
			expiration_date = datetime.strptime(expiration, '%Y-%m-%dT%H:%M:%S')
			if expiration_date <= datetime.now():
				return jsonify({'error': 'Expiration date must be in the future'}), 400
		except ValueError:
			return jsonify({'error': 'Invalid date format. Use YYYY-MM-DDTHH:MM:SS'}), 400

	# Create URL object and store in database
	url = URL(original_url, custom_alias, username, 0, [], expiration)
	urls[custom_alias] = url

	# If user is provided, add URL to user's list
	if username:
		users[username].urls.append(url)

	return jsonify({'shortened_url': custom_alias}), 200

@app.route('/<alias>', methods=['GET'])
def redirect_url(alias):
	# Check if URL exists
	if alias not in urls:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL is expired
	if urls[alias].expiration and urls[alias].expiration < datetime.now():
		return jsonify({'error': 'URL is expired'}), 400

	# Increment click count and add click data
	urls[alias].clicks += 1
	urls[alias].click_data.append({'time': datetime.now().isoformat()})

	# Redirect to original URL
	return redirect(urls[alias].original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')

	# Check if user exists
	if username not in users:
		return jsonify({'error': 'User not found'}), 404

	# Get user's URLs and their analytics
	user_urls = users[username].urls
	analytics = [{'original': url.original, 'shortened': url.shortened, 'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls]

	return jsonify(analytics), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username already exists
	if username in users:
		return jsonify({'error': 'Username already exists'}), 400

	# Hash the password before storing
	hashed_password = hashlib.sha256(password.encode()).hexdigest()

	# Create user and store in database
	user = User(username, hashed_password, [])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
