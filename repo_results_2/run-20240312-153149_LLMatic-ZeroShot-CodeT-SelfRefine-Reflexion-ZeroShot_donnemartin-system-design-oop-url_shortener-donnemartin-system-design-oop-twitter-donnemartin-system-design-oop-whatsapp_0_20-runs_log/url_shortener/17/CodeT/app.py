from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests

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
	created_at: datetime
	expires_at: datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = data.get('short')
	username = data.get('username')
	expires_at = data.get('expires_at')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if short URL is available
	if short_url in urls:
		return jsonify({'error': 'Short URL is already in use'}), 400

	# Create URL object and store in database
	url = URL(original_url, short_url, username, 0, datetime.now(), expires_at)
	urls[short_url] = url

	# Add URL to user's list
	if username:
		users[username].urls.append(url)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Increment click count
	url.clicks += 1

	return redirect(url.original, code=302)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is available
	if username in users:
		return jsonify({'error': 'Username is already in use'}), 400

	# Create user and store in database
	user = User(username, password, [])
	users[username] = user

	return jsonify({'message': 'User created successfully'}), 200

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)
	if not user:
		return jsonify({'error': 'User not found'}), 404

	# Return user's URLs
	return jsonify({'urls': [url.shortened for url in user.urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
