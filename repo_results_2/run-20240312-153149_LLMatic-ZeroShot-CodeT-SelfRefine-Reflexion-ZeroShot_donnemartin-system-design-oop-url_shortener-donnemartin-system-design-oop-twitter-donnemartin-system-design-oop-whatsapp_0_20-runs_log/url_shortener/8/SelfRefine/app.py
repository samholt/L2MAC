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
	# TODO: Add actual URL validation

	# Generate shortened URL
	if custom_alias:
		shortened_url = custom_alias
	else:
		shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

	# Create URL object
	url = URL(original=original_url, shortened=shortened_url, user=username, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S'))

	# Add URL to database
	urls[shortened_url] = url

	# Add URL to user's list
	if username:
		if username in users:
			users[username].urls.append(url)
		else:
			return jsonify({'error': 'User not found'}), 404

	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
	url = urls.get(shortened_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 410

	# Increment click count and add click data
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.now().isoformat()})

	return redirect(url.original, code=302)

@app.route('/analytics/<shortened_url>', methods=['GET'])
def get_analytics(shortened_url):
	url = urls.get(shortened_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	return jsonify({'clicks': url.clicks, 'click_data': url.click_data}), 200

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Create user object
	user = User(username=username, password=password, urls=[])

	# Add user to database
	users[username] = user

	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users.get(username)

	if not user:
		return jsonify({'error': 'User not found'}), 404

	return jsonify({'username': user.username, 'urls': [url.shortened for url in user.urls]}), 200

@app.route('/admin', methods=['GET'])
def get_all_urls():
	return jsonify({'urls': [url.shortened for url in urls.values()]}), 200

@app.route('/admin/<shortened_url>', methods=['DELETE'])
def delete_url(shortened_url):
	url = urls.get(shortened_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Remove URL from user's list
	if url.user:
		users[url.user].urls.remove(url)

	# Remove URL from database
	del urls[shortened_url]

	return jsonify({'message': 'URL deleted'}), 200

@app.route('/admin/user/<username>', methods=['DELETE'])
def delete_user(username):
	user = users.get(username)

	if not user:
		return jsonify({'error': 'User not found'}), 404

	# Remove all of user's URLs
	for url in user.urls:
		del urls[url.shortened]

	# Remove user from database
	del users[username]

	return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
