from flask import Flask, request, jsonify, redirect
import string
import random
from datetime import datetime
import pytz

app = Flask(__name__)

# Mock databases
url_db = {}
user_db = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Validate username and password
	if not username or not password:
		return jsonify({'error': 'Missing username or password'}), 400

	# Check if username is available
	if username in user_db:
		return jsonify({'error': 'Username already in use'}), 400

	# Create user account
	user_db[username] = {'password': password, 'urls': []}

	return jsonify({'message': 'Account created successfully'}), 200

@app.route('/manage_url', methods=['POST'])
def manage_url():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	action = data.get('action')
	short_link = data.get('short_link')

	# Validate input
	if not username or not password or not action or not short_link:
		return jsonify({'error': 'Missing input'}), 400

	# Check if user account exists and password is correct
	if username not in user_db or user_db[username]['password'] != password:
		return jsonify({'error': 'Invalid username or password'}), 401

	# Check if short link exists
	if short_link not in url_db:
		return jsonify({'error': 'Invalid short link'}), 404

	# Perform action
	if action == 'delete':
		url_db.pop(short_link)
		user_db[username]['urls'].remove(short_link)
	elif action == 'edit':
		new_url = data.get('new_url')
		if not new_url:
			return jsonify({'error': 'Missing new URL'}), 400
		url_db[short_link]['url'] = new_url
	else:
		return jsonify({'error': 'Invalid action'}), 400

	return jsonify({'message': 'Action performed successfully'}), 200

@app.route('/view_analytics', methods=['POST'])
def view_analytics():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	# Validate username and password
	if not username or not password:
		return jsonify({'error': 'Missing username or password'}), 400

	# Check if user account exists and password is correct
	if username not in user_db or user_db[username]['password'] != password:
		return jsonify({'error': 'Invalid username or password'}), 401

	# Get analytics for all user's URLs
	analytics = {url: url_db[url]['clicks'] for url in user_db[username]['urls']}

	return jsonify(analytics)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	original_url = data.get('url')
	custom_short_link = data.get('custom_short_link')
	expiration = data.get('expiration')

	# Validate input
	if not username or not password or not original_url:
		return jsonify({'error': 'Missing input'}), 400

	# Check if user account exists and password is correct
	if username not in user_db or user_db[username]['password'] != password:
		return jsonify({'error': 'Invalid username or password'}), 401

	# Check if custom short link is available
	if custom_short_link and custom_short_link in url_db:
		return jsonify({'error': 'Custom short link already in use'}), 400

	# Generate unique short link
	short_link = custom_short_link if custom_short_link else ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	while short_link in url_db:
		short_link = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

	# Store in mock databases
	url_db[short_link] = {'url': original_url, 'clicks': [], 'expiration': expiration}
	user_db[username]['urls'].append(short_link)

	return jsonify({'short_link': short_link}), 200

@app.route('/<short_link>', methods=['GET'])
def redirect_url(short_link):
	# Check if short link exists in database
	if short_link not in url_db:
		return jsonify({'error': 'Invalid short link'}), 404

	# Check if URL is expired
	if url_db[short_link]['expiration'] and datetime.now(pytz.utc) > datetime.fromisoformat(url_db[short_link]['expiration']):
		return jsonify({'error': 'URL is expired'}), 404

	# Record click
	click = {'timestamp': datetime.now(pytz.utc).isoformat(), 'location': request.remote_addr}
	url_db[short_link]['clicks'].append(click)

	# Redirect to original URL
	return redirect(url_db[short_link]['url'], code=302)

@app.route('/stats/<short_link>', methods=['GET'])
def get_stats(short_link):
	# Check if short link exists in database
	if short_link not in url_db:
		return jsonify({'error': 'Invalid short link'}), 404

	# Return statistics
	return jsonify(url_db[short_link]['clicks'])

# Admin dashboard
@app.route('/admin/urls', methods=['GET'])
def admin_view_urls():
	# Return all URLs
	return jsonify(list(url_db.keys()))

@app.route('/admin/url/<short_link>', methods=['DELETE'])
def admin_delete_url(short_link):
	# Check if short link exists
	if short_link not in url_db:
		return jsonify({'error': 'Invalid short link'}), 404

	# Delete URL
	url_db.pop(short_link)
	for user in user_db.values():
		if short_link in user['urls']:
			user['urls'].remove(short_link)

	return jsonify({'message': 'URL deleted successfully'}), 200

@app.route('/admin/user/<username>', methods=['DELETE'])
def admin_delete_user(username):
	# Check if user exists
	if username not in user_db:
		return jsonify({'error': 'Invalid username'}), 404

	# Delete user
	user_db.pop(username)

	return jsonify({'message': 'User deleted successfully'}), 200

@app.route('/admin/analytics', methods=['GET'])
def admin_view_analytics():
	# Calculate analytics
	total_users = len(user_db)
	total_urls = len(url_db)
	total_clicks = sum(len(url['clicks']) for url in url_db.values())

	return jsonify({'total_users': total_users, 'total_urls': total_urls, 'total_clicks': total_clicks})

if __name__ == '__main__':
	app.run(debug=True)
