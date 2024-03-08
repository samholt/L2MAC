from flask import Flask, request, jsonify, redirect, session
import validators
from datetime import datetime
import hashlib

app = Flask(__name__)
app.secret_key = 'super secret key'

# Mock database
url_db = {}

# Mock analytics database
analytics_db = {}

# Mock user database
user_db = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if username in user_db:
		return jsonify({'error': 'Username already exists'}), 400
	user_db[username] = hashlib.md5(password.encode()).hexdigest()
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if username not in user_db or user_db[username] != hashlib.md5(password.encode()).hexdigest():
		return jsonify({'error': 'Invalid username or password'}), 400
	session['username'] = username
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['GET'])
def logout():
	if 'username' in session:
		session.pop('username')
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	if 'username' not in session:
		return jsonify({'error': 'Please log in'}), 401
	url = request.json.get('url')
	if not validators.url(url):
		return jsonify({'error': 'Invalid URL'}), 400
	short_url = session['username']
	# Store the original URL and the shortened URL in the mock database
	if session['username'] not in url_db:
		url_db[session['username']] = {}
	url_db[session['username']][short_url] = url
	return jsonify({'short_url': 'http://short.url/' + short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	# Look up the original URL associated with the shortened URL
	original_url = None
	for user in url_db:
		original_url = url_db[user].get(short_url)
		if original_url is not None:
			break
	if original_url is None:
		return jsonify({'error': 'URL not found'}), 404
	# Record the access in the analytics database
	if short_url not in analytics_db:
		analytics_db[short_url] = []
	analytics_db[short_url].append({'access_time': datetime.now().isoformat(), 'location': 'Placeholder Location'})
	# Redirect the user to the original URL
	return redirect(original_url, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	# Look up the analytics for the shortened URL
	analytics = analytics_db.get(short_url)
	if analytics is None:
		return jsonify({'error': 'URL not found'}), 404
	# Return the analytics
	return jsonify({'analytics': analytics}), 200

@app.route('/user/urls', methods=['GET'])
def get_user_urls():
	if 'username' not in session:
		return jsonify({'error': 'Please log in'}), 401
	urls = url_db.get(session['username'])
	if urls is None:
		return jsonify({'error': 'No URLs found'}), 404
	return jsonify({'urls': urls}), 200

@app.route('/user/analytics', methods=['GET'])
def get_user_analytics():
	if 'username' not in session:
		return jsonify({'error': 'Please log in'}), 401
	urls = url_db.get(session['username'])
	if urls is None:
		return jsonify({'error': 'No URLs found'}), 404
	user_analytics = {url: analytics_db.get(url) for url in urls}
	return jsonify({'analytics': user_analytics}), 200

if __name__ == '__main__':
	app.run(debug=True)
