from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string
import re

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
	url_regex = re.compile(
		'r^(?:http|ftp)s?://' # http:// or https://
		'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		'localhost|' #localhost...
		'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		'(?::\d+)?' # optional port
		'(?:/?|[/?]\S+)$', re.IGNORECASE)
	if re.match(url_regex, original_url) is None:
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if custom_short:
		short_url = custom_short

	# Create URL object
	url = URL(original=original_url, short=short_url, user=username, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S'))

	# Add URL to database
	urls[short_url] = url

	# Add URL to user's list
	if username and username in users:
		users[username].urls.append(url)

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and datetime.now() <= url.expiration:
		url.clicks += 1
		url.click_data.append({'click_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'location': request.remote_addr})
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')
	if username and username in users:
		user_urls = users[username].urls
		analytics = [{'original': url.original, 'short': url.short, 'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls]
		return jsonify(analytics), 200
	else:
		return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Create user object
	user = User(username=username, password=password, urls=[])

	# Add user to database
	users[username] = user

	return jsonify({'message': 'User created'}), 201

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	# TODO: Add authentication
	all_urls = [{'original': url.original, 'short': url.short, 'user': url.user, 'clicks': url.clicks, 'click_data': url.click_data} for url in urls.values()]
	return jsonify(all_urls), 200

if __name__ == '__main__':
	app.run(debug=True)
