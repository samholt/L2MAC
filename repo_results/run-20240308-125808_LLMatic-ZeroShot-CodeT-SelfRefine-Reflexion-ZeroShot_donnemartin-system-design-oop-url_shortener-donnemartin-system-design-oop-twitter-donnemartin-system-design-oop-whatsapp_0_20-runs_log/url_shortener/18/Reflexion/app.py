from flask import Flask, request, redirect, jsonify
import random
import string
from dataclasses import dataclass
from datetime import datetime
import requests
from geolite2 import geolite2

app = Flask(__name__)

# Mock database
DATABASE = {}

# Mock user database
USER_DATABASE = {}

# Mock admin database
ADMIN_DATABASE = {}

# Mock analytics database
ANALYTICS_DATABASE = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	expiration: datetime

@dataclass
class User:
	username: str
	password: str

@dataclass
class Admin:
	username: str
	password: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = data.get('short_url')
	user = data.get('user')
	expiration = data.get('expiration')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL if not provided
	if not short_url:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

	# Check if short URL is already in use
	if short_url in DATABASE:
		return jsonify({'error': 'Short URL already in use'}), 400

	# Create URL object and store in database
	url = URL(original_url, short_url, user, expiration)
	DATABASE[short_url] = url

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DATABASE.get(short_url)

	# Check if URL exists
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expiration and url.expiration < datetime.now():
		return jsonify({'error': 'URL has expired'}), 410

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# Check if user exists
	if user not in USER_DATABASE:
		return jsonify({'error': 'User not found'}), 404

	# Get user's URLs
	urls = [url for url in DATABASE.values() if url.user == user]

	# Get analytics for each URL
	analytics = {url.shortened: ANALYTICS_DATABASE.get(url.shortened, []) for url in urls}

	return jsonify(analytics), 200

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already in use
	if username in USER_DATABASE:
		return jsonify({'error': 'Username already in use'}), 400

	# Create user and store in database
	user = User(username, password)
	USER_DATABASE[username] = user

	return jsonify({'message': 'User created'}), 201

@app.route('/admin', methods=['POST'])
def create_admin():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Check if username is already in use
	if username in ADMIN_DATABASE:
		return jsonify({'error': 'Username already in use'}), 400

	# Create admin and store in database
	admin = Admin(username, password)
	ADMIN_DATABASE[username] = admin

	return jsonify({'message': 'Admin created'}), 201

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	data = request.get_json()
	admin = data.get('admin')

	# Check if admin exists
	if admin not in ADMIN_DATABASE:
		return jsonify({'error': 'Admin not found'}), 404

	# Get all URLs
	urls = list(DATABASE.values())

	return jsonify([url.__dict__ for url in urls]), 200

if __name__ == '__main__':
	app.run(debug=True)

