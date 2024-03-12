from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}
users_db = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	click_data: list
	expiration: datetime.datetime

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

	# Check if custom alias is already in use
	if custom_alias and custom_alias in urls_db:
		return jsonify({'error': 'Alias already in use'}), 400

	# Generate random alias if not provided
	if not custom_alias:
		custom_alias = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

	# Create URL object and store in database
	url = URL(original=original_url, shortened=custom_alias, user=username, clicks=0, click_data=[], expiration=expiration)
	urls_db[custom_alias] = url

	# Add URL to user's list of URLs
	if username:
		users_db[username].urls.append(url)

	return jsonify({'shortened_url': custom_alias}), 200

@app.route('/<alias>', methods=['GET'])
def redirect_url(alias):
	# Check if URL exists
	if alias not in urls_db:
		return jsonify({'error': 'URL not found'}), 404

	url = urls_db[alias]

	# Check if URL has expired
	if url.expiration and datetime.datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 410

	# Increment click count and store click data
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.datetime.now().isoformat()})

	return redirect(url.original, code=302)

@app.route('/analytics/<alias>', methods=['GET'])
def get_analytics(alias):
	# Check if URL exists
	if alias not in urls_db:
		return jsonify({'error': 'URL not found'}), 404

	url = urls_db[alias]

	# Return analytics data
	return jsonify({'clicks': url.clicks, 'click_data': url.click_data}), 200

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already in use
	if username in users_db:
		return jsonify({'error': 'Username already in use'}), 400

	# Create User object and store in database
	user = User(username=username, password=password, urls=[])
	users_db[username] = user

	return jsonify({'message': 'User created successfully'}), 200

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	# Check if user exists
	if username not in users_db:
		return jsonify({'error': 'User not found'}), 404

	user = users_db[username]

	# Return user data
	return jsonify({'username': user.username, 'urls': [url.shortened for url in user.urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
