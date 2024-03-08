from flask import Flask, request, jsonify, redirect
import string
import random
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

class Database:
	def __init__(self):
		self.user_db = {}
		self.url_db = {}
		self.analytics_db = {}

db = Database()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if not data or 'username' not in data or 'password' not in data:
		return jsonify({'error': 'Username and password are required'}), 400
	username = data['username']
	password = data['password']
	if username in db.user_db:
		return jsonify({'error': 'Username is already in use'}), 400
	db.user_db[username] = generate_password_hash(password)
	db.url_db[username] = {}
	db.analytics_db[username] = {}
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if not data or 'username' not in data or 'password' not in data:
		return jsonify({'error': 'Username and password are required'}), 400
	username = data['username']
	password = data['password']
	if username not in db.user_db or not check_password_hash(db.user_db[username], password):
		return jsonify({'error': 'Invalid username or password'}), 401
	return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		data = request.get_json()
		if not data or 'username' not in data or 'url' not in data:
			return jsonify({'error': 'Username and URL are required'}), 400
		username = data['username']
		url = data['url']
		custom = data.get('custom')
		expiration = data.get('expiration')
		if username not in db.user_db:
			return jsonify({'error': 'User not found'}), 404
		if custom:
			if custom in db.url_db[username]:
				return jsonify({'error': 'Custom URL is already in use'}), 400
			else:
				db.url_db[username][custom] = {'url': url, 'expiration': expiration}
				db.analytics_db[username][custom] = {'clicks': 0, 'timestamps': [], 'locations': []}
				return jsonify({'short_url': custom}), 201
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			while short_url in db.url_db[username]:
				short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			db.url_db[username][short_url] = {'url': url, 'expiration': expiration}
			db.analytics_db[username][short_url] = {'clicks': 0, 'timestamps': [], 'locations': []}
			return jsonify({'short_url': short_url}), 201
	return 'Hello, World!'

@app.route('/<username>/<short_url>', methods=['GET'])
def redirect_url(username, short_url):
	if username in db.url_db and short_url in db.url_db[username]:
		if db.url_db[username][short_url]['expiration'] and datetime.now() > datetime.fromisoformat(db.url_db[username][short_url]['expiration']):
			return jsonify({'error': 'URL has expired'}), 404
		db.analytics_db[username][short_url]['clicks'] += 1
		db.analytics_db[username][short_url]['timestamps'].append(datetime.now().isoformat())
		db.analytics_db[username][short_url]['locations'].append(request.remote_addr)
		return redirect(db.url_db[username][short_url]['url'], code=302)
	else:
		return jsonify({'error': 'URL not found'}), 404

@app.route('/admin', methods=['GET', 'DELETE'])
def admin():
	if request.method == 'GET':
		return jsonify({'users': list(db.user_db.keys()), 'urls': db.url_db, 'analytics': db.analytics_db}), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		if not data or 'username' not in data:
			return jsonify({'error': 'Username is required'}), 400
		username = data['username']
		short_url = data.get('short_url')
		if short_url:
			if username in db.url_db and short_url in db.url_db[username]:
				del db.url_db[username][short_url]
				del db.analytics_db[username][short_url]
				return jsonify({'message': 'URL deleted successfully'}), 200
			else:
				return jsonify({'error': 'URL not found'}), 404
		else:
			if username in db.user_db:
				del db.user_db[username]
				del db.url_db[username]
				del db.analytics_db[username]
				return jsonify({'message': 'User deleted successfully'}), 200
			else:
				return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
