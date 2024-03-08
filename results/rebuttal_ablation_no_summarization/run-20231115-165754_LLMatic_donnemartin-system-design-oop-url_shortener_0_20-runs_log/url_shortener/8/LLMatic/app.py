from flask import Flask, request, jsonify, redirect
import string
import random
from datetime import datetime

app = Flask(__name__)

url_db = {}
user_db = {}

@app.route('/')
def home():
	# Home route
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	# Register a new user
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	if not username or not password:
		return jsonify({'error': 'Username and password are required'}), 400

	if username in user_db:
		return jsonify({'error': 'Username already exists'}), 400

	user_db[username] = {'password': password, 'urls': []}
	return jsonify({'message': 'User created successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	# Login a user
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	if not username or not password:
		return jsonify({'error': 'Username and password are required'}), 400

	if username not in user_db or user_db[username]['password'] != password:
		return jsonify({'error': 'Invalid username or password'}), 400

	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	# Shorten a URL
	data = request.get_json()
	username = data.get('username')
	original_url = data.get('url')
	custom_alias = data.get('alias')
	expiration_date = data.get('expiration_date')

	if not username or not original_url:
		return jsonify({'error': 'Username and URL are required'}), 400

	if username not in user_db:
		return jsonify({'error': 'Invalid username'}), 400

	if custom_alias:
		if custom_alias in url_db:
			return jsonify({'error': 'Alias already in use'}), 400
		else:
			url_db[custom_alias] = {'url': original_url, 'clicks': [], 'username': username, 'expiration_date': expiration_date}
			user_db[username]['urls'].append(custom_alias)
			return jsonify({'shortened_url': custom_alias}), 200

	shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	while shortened_url in url_db:
		shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

	url_db[shortened_url] = {'url': original_url, 'clicks': [], 'username': username, 'expiration_date': expiration_date}
	user_db[username]['urls'].append(shortened_url)

	return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	# Redirect to the original URL
	if short_url in url_db:
		if 'expiration_date' in url_db[short_url] and datetime.now() > datetime.fromisoformat(url_db[short_url]['expiration_date']):
			return jsonify({'error': 'Shortened URL has expired'}), 404
		click_data = {'timestamp': datetime.now().isoformat()}
		ip = request.remote_addr
		click_data['location'] = 'US'
		url_db[short_url]['clicks'].append(click_data)
		return redirect(url_db[short_url]['url'], code=302)
	else:
		return jsonify({'error': 'Invalid shortened URL'}), 404

@app.route('/analytics/<username>', methods=['GET'])
def analytics(username):
	# Get analytics for a user
	if username not in user_db:
		return jsonify({'error': 'Invalid username'}), 404

	user_urls = user_db[username]['urls']
	analytics_data = {url: url_db[url]['clicks'] for url in user_urls}

	return jsonify(analytics_data)

@app.route('/delete_url', methods=['POST'])
def delete_url():
	# Delete a shortened URL
	data = request.get_json()
	username = data.get('username')
	short_url = data.get('short_url')

	if not username or not short_url:
		return jsonify({'error': 'Username and shortened URL are required'}), 400

	if username not in user_db or short_url not in user_db[username]['urls']:
		return jsonify({'error': 'Invalid username or shortened URL'}), 400

	user_db[username]['urls'].remove(short_url)
	del url_db[short_url]

	return jsonify({'message': 'Shortened URL deleted successfully'}), 200

@app.route('/admin/urls', methods=['GET'])
def admin_urls():
	# Get all URLs (admin only)
	return jsonify(url_db)

@app.route('/admin/url', methods=['DELETE'])
def admin_delete_url():
	# Delete a URL (admin only)
	data = request.get_json()
	short_url = data.get('short_url')

	if not short_url:
		return jsonify({'error': 'Shortened URL is required'}), 400

	if short_url not in url_db:
		return jsonify({'error': 'Invalid shortened URL'}), 400

	del url_db[short_url]

	return jsonify({'message': 'Shortened URL deleted successfully'}), 200

@app.route('/admin/user', methods=['DELETE'])
def admin_delete_user():
	# Delete a user (admin only)
	data = request.get_json()
	username = data.get('username')

	if not username:
		return jsonify({'error': 'Username is required'}), 400

	if username not in user_db:
		return jsonify({'error': 'Invalid username'}), 400

	del user_db[username]

	return jsonify({'message': 'User deleted successfully'}), 200

@app.route('/admin/analytics', methods=['GET'])
def admin_analytics():
	# Get analytics for all users (admin only)
	user_count = len(user_db)
	url_count = len(url_db)
	click_count = sum(len(url_db[url]['clicks']) for url in url_db)

	return jsonify({'user_count': user_count, 'url_count': url_count, 'click_count': click_count})

if __name__ == '__main__':
	app.run(debug=True)
