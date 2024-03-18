from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import string
import random
from geolite2 import geolite2
import requests

app = Flask(__name__)

# Mock database
DB = {}

# Mock user database
USERS = {}

# Mock admin database
ADMINS = {}

# URL validation function
def validate_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False

# URL shortening function
@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_alias = data.get('custom_alias')
	user_id = data.get('user_id')
	expiration_date = data.get('expiration_date')

	if not validate_url(url):
		return jsonify({'error': 'Invalid URL'}), 400

	if custom_alias:
		if custom_alias in DB:
			return jsonify({'error': 'Custom alias already in use'}), 400
		else:
			short_url = custom_alias
	else:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

	DB[short_url] = {
		'url': url,
		'clicks': [],
		'user_id': user_id,
		'expiration_date': expiration_date
	}

	return jsonify({'short_url': short_url}), 200

# URL redirection function
@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url_data = DB.get(short_url)

	if not url_data:
		return jsonify({'error': 'URL not found'}), 404

	if url_data.get('expiration_date') and datetime.now() > url_data.get('expiration_date'):
		return jsonify({'error': 'URL expired'}), 410

	url_data['clicks'].append({
		'time': datetime.now(),
		'location': geolite2.reader().get(request.remote_addr)
	})

	return redirect(url_data['url'], code=302)

# Analytics function
@app.route('/analytics', methods=['GET'])
def get_analytics():
	user_id = request.args.get('user_id')

	if not user_id in USERS:
		return jsonify({'error': 'User not found'}), 404

	user_urls = [url for url in DB.values() if url['user_id'] == user_id]

	return jsonify(user_urls), 200

# User account creation function
@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user_id = data.get('user_id')

	if user_id in USERS:
		return jsonify({'error': 'User already exists'}), 400

	USERS[user_id] = {
		'user_id': user_id,
		'urls': []
	}

	return jsonify({'message': 'User created'}), 201

# Admin dashboard function
@app.route('/admin', methods=['GET'])
def admin_dashboard():
	admin_id = request.args.get('admin_id')

	if not admin_id in ADMINS:
		return jsonify({'error': 'Admin not found'}), 404

	return jsonify({'users': USERS, 'urls': DB}), 200

if __name__ == '__main__':
	app.run(debug=True)
