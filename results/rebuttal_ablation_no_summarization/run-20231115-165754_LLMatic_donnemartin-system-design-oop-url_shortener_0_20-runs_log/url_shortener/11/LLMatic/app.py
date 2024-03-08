import random
import string
import requests
from flask import Flask, request, redirect, jsonify
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock database
DATABASE = {}
ANALYTICS = {}
USERS = {}

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	
	if username in USERS:
		return jsonify({'message': 'Username already exists'}), 400
	
	USERS[username] = {
		'password': generate_password_hash(password),
		'urls': {}
	}
	
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	
	if username not in USERS or not check_password_hash(USERS[username]['password'], password):
		return jsonify({'message': 'Invalid username or password'}), 400
	
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/urls', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/shorten', methods=['POST'])
def manage_urls():
	username = request.json.get('username')
	short_url = request.json.get('short_url')
	
	if request.method == 'GET':
		if username not in USERS:
			return jsonify({'message': 'User not found'}), 404
		
		return jsonify(USERS[username]['urls'])
	
	elif request.method == 'POST':
		url = request.json.get('url')
		expiration = request.json.get('expiration')
		
		# Validate URL
		try:
			response = requests.get(url)
			if response.status_code != 200:
				return jsonify({'message': 'Invalid URL'}), 400
		except:
			return jsonify({'message': 'Invalid URL'}), 400
		
		# Generate short URL
		if short_url and short_url not in DATABASE:
			short_url = short_url
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			while short_url in DATABASE:
				short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		
		# Store in database
		DATABASE[short_url] = {'url': url, 'expiration': expiration}
		ANALYTICS[short_url] = {'clicks': 0, 'click_data': []}
		USERS[username]['urls'][short_url] = url
		
		return jsonify({'short_url': short_url})
	
	elif request.method == 'PUT':
		new_url = request.json.get('new_url')
		
		# Validate new URL
		try:
			response = requests.get(new_url)
			if response.status_code != 200:
				return jsonify({'message': 'Invalid URL'}), 400
		except:
			return jsonify({'message': 'Invalid URL'}), 400
		
		# Update URL
		if short_url in DATABASE and short_url in USERS[username]['urls']:
			DATABASE[short_url]['url'] = new_url
			USERS[username]['urls'][short_url] = new_url
			
			return jsonify({'message': 'URL updated successfully'})
		
		return jsonify({'message': 'URL not found'}), 404
	
	elif request.method == 'DELETE':
		# Delete URL
		if short_url in DATABASE and short_url in USERS[username]['urls']:
			del DATABASE[short_url]
			del ANALYTICS[short_url]
			del USERS[username]['urls'][short_url]
			
			return jsonify({'message': 'URL deleted successfully'})
		
		return jsonify({'message': 'URL not found'}), 404

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in DATABASE:
		url = DATABASE[short_url]['url']
		ANALYTICS[short_url]['clicks'] += 1
		ANALYTICS[short_url]['click_data'].append({'timestamp': datetime.now().isoformat()})
		return redirect(url)
	else:
		return jsonify({'message': 'URL not found'}), 404

@app.route('/analytics', methods=['GET'])
def view_user_analytics():
	username = request.json.get('username')
	
	if username not in USERS:
		return jsonify({'message': 'User not found'}), 404
	
	user_analytics = {}
	for short_url in USERS[username]['urls']:
		if short_url in ANALYTICS:
			user_analytics[short_url] = ANALYTICS[short_url]
	
	return jsonify(user_analytics)

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return jsonify({'users': USERS, 'urls': DATABASE, 'analytics': ANALYTICS})
	elif request.method == 'DELETE':
		username = request.json.get('username')
		short_url = request.json.get('short_url')
		
		if username and username in USERS:
			del USERS[username]
			return jsonify({'message': 'User deleted successfully'})
		elif short_url and short_url in DATABASE:
			del DATABASE[short_url]
			del ANALYTICS[short_url]
			for user in USERS.values():
				if short_url in user['urls']:
					del user['urls'][short_url]
			return jsonify({'message': 'URL deleted successfully'})
		
		return jsonify({'message': 'Invalid request'}), 400

if __name__ == '__main__':
	app.run(debug=True)
