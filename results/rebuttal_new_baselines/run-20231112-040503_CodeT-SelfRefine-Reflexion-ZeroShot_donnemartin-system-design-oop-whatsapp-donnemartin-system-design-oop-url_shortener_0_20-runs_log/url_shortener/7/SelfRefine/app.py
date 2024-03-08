from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import string
import random

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
	if not original_url:
		return jsonify({'error': 'URL is required'}), 400

	# Check if URL has already been shortened by the user
	if user in users and original_url in [url.original for url in users[user].urls]:
		return jsonify({'error': 'URL has already been shortened'}), 400

	# Generate shortened URL
	shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom:
		if custom in urls:
			return jsonify({'error': 'Custom URL is already in use'}), 400
		shortened_url = custom

	# Create URL object
	url = URL(original=original_url, shortened=shortened_url, user=user, clicks=0, click_data=[], expiration=expiration)
	urls[shortened_url] = url

	# Add URL to user's list of URLs
	if user in users:
		users[user].urls.append(url)

	return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = urls.get(shortened_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expiration and datetime.now() > url.expiration:
		del urls[shortened_url]
		return jsonify({'error': 'URL has expired'}), 404

	# Increment clicks
	url.clicks += 1
	url.click_data.append({'click_time': datetime.now().isoformat()})

	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# Validate user
	if not user:
		return jsonify({'error': 'User is required'}), 400

	user_urls = [url for url in urls.values() if url.user == user]
	analytics = [{'original': url.original, 'shortened': url.shortened, 'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls]

	return jsonify(analytics), 200

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Validate user
	if not username or not password:
		return jsonify({'error': 'Username and password are required'}), 400

	# Create user object
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User created successfully'}), 200

@app.route('/users/<username>/urls', methods=['GET'])
def get_user_urls(username):
	user = users.get(username)
	if not user:
		return jsonify({'error': 'User not found'}), 404

	user_urls = [{'original': url.original, 'shortened': url.shortened} for url in user.urls]

	return jsonify(user_urls), 200

@app.route('/admin/urls', methods=['GET'])
def get_all_urls():
	all_urls = [{'original': url.original, 'shortened': url.shortened, 'user': url.user} for url in urls.values()]

	return jsonify(all_urls), 200

@app.route('/admin/users', methods=['GET'])
def get_all_users():
	all_users = [{'username': user.username, 'urls': [{'original': url.original, 'shortened': url.shortened} for url in user.urls]} for user in users.values()]

	return jsonify(all_users), 200

@app.route('/admin/users/<username>', methods=['DELETE'])
def delete_user(username):
	user = users.get(username)
	if not user:
		return jsonify({'error': 'User not found'}), 404

	del users[username]

	return jsonify({'message': 'User deleted successfully'}), 200

@app.route('/admin/urls/<shortened_url>', methods=['DELETE'])
def delete_url(shortened_url):
	url = urls.get(shortened_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	del urls[shortened_url]

	return jsonify({'message': 'URL deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
