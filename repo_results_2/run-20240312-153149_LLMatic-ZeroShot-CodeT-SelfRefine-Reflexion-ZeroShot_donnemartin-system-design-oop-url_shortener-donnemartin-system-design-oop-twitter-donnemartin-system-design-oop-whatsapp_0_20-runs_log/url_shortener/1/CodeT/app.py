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
	clicks: list
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
	custom_short = data.get('custom_short')
	expiration = data.get('expiration')

	# Validate URL
	if not original_url:
		return jsonify({'error': 'URL is required'}), 400

	# Generate short URL
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom_short:
		short_url = custom_short

	# Create URL object
	url = URL(original=original_url, short=short_url, user=user, clicks=[], expiration=expiration)
	urls[short_url] = url

	# Add URL to user's list
	if user:
		users[user].urls.append(url)

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Add click data
	url.clicks.append({'time': datetime.now(), 'location': request.remote_addr})

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# Get user's URLs
	user_urls = users[user].urls

	# Get analytics for each URL
	analytics = []
	for url in user_urls:
		analytics.append({'short': url.short, 'clicks': len(url.clicks), 'last_clicked': url.clicks[-1] if url.clicks else None})

	return jsonify(analytics), 200

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Validate input
	if not username or not password:
		return jsonify({'error': 'Username and password are required'}), 400

	# Create user
	user = User(username=username, password=password, urls=[])
	users[username] = user

	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	# Get all URLs
	all_urls = [{'short': url.short, 'original': url.original, 'user': url.user, 'clicks': len(url.clicks)} for url in urls.values()]

	return jsonify(all_urls), 200

@app.route('/delete', methods=['DELETE'])
def delete_url():
	data = request.get_json()
	short_url = data.get('short_url')
	user = data.get('user')

	# Validate input
	if not short_url:
		return jsonify({'error': 'Short URL is required'}), 400

	# Delete URL
	del urls[short_url]

	# Remove URL from user's list
	if user:
		users[user].urls = [url for url in users[user].urls if url.short != short_url]

	return jsonify({'message': 'URL deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
