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
	user = data.get('user')
	custom = data.get('custom')
	expiration = data.get('expiration')

	# Validate URL
	# For now, we just check if it starts with http
	if not original_url.startswith('http'):
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom:
		short_url = custom

	# Create URL object
	url = URL(original_url, short_url, user, 0, [], expiration)

	# Add to database
	urls[short_url] = url

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Increment click count and add click data
	url.clicks += 1
	url.click_data.append({'time': datetime.now().isoformat()})

	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# Get user URLs
	user_urls = [url for url in urls.values() if url.user == user]

	# Return analytics data
	return jsonify({'urls': [url.__dict__ for url in user_urls]}), 200

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Create user object
	user = User(username, password, [])

	# Add to database
	users[username] = user

	return jsonify({'message': 'User created'}), 200

@app.route('/user', methods=['GET'])
def get_user():
	data = request.get_json()
	username = data.get('username')

	# Get user
	user = users.get(username)
	if not user:
		return jsonify({'error': 'User not found'}), 404

	# Return user data
	return jsonify(user.__dict__), 200

@app.route('/admin', methods=['GET'])
def get_admin():
	# Return all URLs and users
	return jsonify({'urls': [url.__dict__ for url in urls.values()], 'users': [user.__dict__ for user in users.values()]}), 200

@app.route('/admin', methods=['DELETE'])
def delete_admin():
	data = request.get_json()
	url = data.get('url')
	user = data.get('user')

	# Delete URL or user
	if url:
		del urls[url]
	if user:
		del users[user]

	return jsonify({'message': 'Deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
