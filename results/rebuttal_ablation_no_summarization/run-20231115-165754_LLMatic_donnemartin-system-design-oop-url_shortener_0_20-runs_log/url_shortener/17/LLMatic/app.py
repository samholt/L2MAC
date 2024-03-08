import string
import random
from flask import Flask, request, redirect, jsonify
from urllib.parse import urlparse
from datetime import datetime
import pytz
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Mock database
DATABASE = {}

# Mock analytics database
ANALYTICS = {}

# Mock user accounts database
USER_ACCOUNTS = {}

# Mock admin accounts database
ADMIN_ACCOUNTS = {}

# User Account class
class UserAccount:
	def __init__(self, username):
		self.username = username
		self.urls = {}
		self.analytics = {}

# Admin Account class
class AdminAccount:
	def __init__(self, username):
		self.username = username
		self.urls = DATABASE
		self.analytics = ANALYTICS

@app.route('/')
def home():
	logging.info('Home page accessed')
	return 'Welcome to the URL Shortener Service!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	custom_short_url = request.json.get('custom_short_url')
	username = request.json.get('username')
	expiration_date = request.json.get('expiration_date')

	# Validate URL
	try:
		parsed_url = urlparse(url)
		if not all([parsed_url.scheme, parsed_url.netloc]):
			return jsonify({'error': 'Invalid URL'}), 400
	except Exception as e:
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if custom short URL is available
	if custom_short_url and custom_short_url in DATABASE:
		return jsonify({'error': 'Custom short URL is already in use'}), 400

	# Generate unique identifier for URL
	short_url = custom_short_url if custom_short_url else ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	while short_url in DATABASE:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

	# Store mapping between original URL and shortened URL
	DATABASE[short_url] = {'url': url, 'expiration_date': expiration_date}

	# Initialize analytics for this short URL
	ANALYTICS[short_url] = []

	# Create a new user account if the username does not exist
	if username not in USER_ACCOUNTS:
		USER_ACCOUNTS[username] = UserAccount(username)
		logging.info(f'User account created: {username}')

	# Associate the shortened URL and its analytics with the user's account
	USER_ACCOUNTS[username].urls[short_url] = url
	USER_ACCOUNTS[username].analytics[short_url] = []

	# Create a new admin account if the username is 'admin'
	if username == 'admin' and username not in ADMIN_ACCOUNTS:
		ADMIN_ACCOUNTS[username] = AdminAccount(username)
		logging.info('Admin account created')

	logging.info(f'URL shortened: {url} -> {short_url}')
	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in DATABASE:
		# Check if the URL has expired
		if DATABASE[short_url]['expiration_date'] and datetime.now(pytz.utc) > datetime.fromisoformat(DATABASE[short_url]['expiration_date']):
			return jsonify({'error': 'URL has expired'}), 400

		# Record access in analytics
		ANALYTICS[short_url].append({'timestamp': datetime.now(pytz.utc).isoformat()})
		logging.info(f'URL redirected: {short_url}')
		return redirect(DATABASE[short_url]['url'], code=302)
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/analytics', methods=['GET'])
def analytics():
	short_url = request.args.get('short_url')
	if short_url in ANALYTICS:
		return jsonify(ANALYTICS[short_url])
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/account', methods=['GET', 'POST', 'DELETE'])
def account():
	username = request.json.get('username')
	if request.method == 'GET':
		# View user's shortened URLs and their analytics
		if username in USER_ACCOUNTS:
			return jsonify({'urls': USER_ACCOUNTS[username].urls, 'analytics': USER_ACCOUNTS[username].analytics})
		else:
			return jsonify({'error': 'User not found'}), 404
	elif request.method == 'POST':
		# Edit user's shortened URLs
		short_url = request.json.get('short_url')
		new_url = request.json.get('new_url')
		if username in USER_ACCOUNTS and short_url in USER_ACCOUNTS[username].urls:
			USER_ACCOUNTS[username].urls[short_url] = new_url
			logging.info(f'User URL updated: {username} -> {short_url} -> {new_url}')
			return jsonify({'message': 'URL updated successfully'})
		else:
			return jsonify({'error': 'User or URL not found'}), 404
	elif request.method == 'DELETE':
		# Delete user's shortened URLs
		short_url = request.json.get('short_url')
		if username in USER_ACCOUNTS and short_url in USER_ACCOUNTS[username].urls:
			del USER_ACCOUNTS[username].urls[short_url]
			logging.info(f'User URL deleted: {username} -> {short_url}')
			return jsonify({'message': 'URL deleted successfully'})
		else:
			return jsonify({'error': 'User or URL not found'}), 404

@app.route('/admin', methods=['GET', 'POST', 'DELETE'])
def admin():
	username = request.json.get('username')
	if request.method == 'GET':
		# View all shortened URLs and their analytics
		if username in ADMIN_ACCOUNTS:
			return jsonify({'urls': ADMIN_ACCOUNTS[username].urls, 'analytics': ADMIN_ACCOUNTS[username].analytics})
		else:
			return jsonify({'error': 'Admin not found'}), 404
	elif request.method == 'POST':
		# Edit any shortened URL
		short_url = request.json.get('short_url')
		new_url = request.json.get('new_url')
		if username in ADMIN_ACCOUNTS and short_url in ADMIN_ACCOUNTS[username].urls:
			ADMIN_ACCOUNTS[username].urls[short_url] = new_url
			logging.info(f'Admin URL updated: {username} -> {short_url} -> {new_url}')
			return jsonify({'message': 'URL updated successfully'})
		else:
			return jsonify({'error': 'Admin or URL not found'}), 404
	elif request.method == 'DELETE':
		# Delete any shortened URL or user account
		short_url = request.json.get('short_url')
		user_to_delete = request.json.get('user_to_delete')
		if username in ADMIN_ACCOUNTS:
			if short_url in ADMIN_ACCOUNTS[username].urls:
				del ADMIN_ACCOUNTS[username].urls[short_url]
				logging.info(f'Admin URL deleted: {username} -> {short_url}')
				return jsonify({'message': 'URL deleted successfully'})
			elif user_to_delete in USER_ACCOUNTS:
				del USER_ACCOUNTS[user_to_delete]
				logging.info(f'User account deleted: {username} -> {user_to_delete}')
				return jsonify({'message': 'User account deleted successfully'})
			else:
				return jsonify({'error': 'URL or user account not found'}), 404
		else:
			return jsonify({'error': 'Admin not found'}), 404

@app.errorhandler(404)
def page_not_found(e):
	logging.error('404 error occurred')
	return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
	logging.error('500 error occurred')
	return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
	app.run(debug=True)
