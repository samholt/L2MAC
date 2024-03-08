from flask import Flask, request, jsonify, redirect, abort, session
import string
import random
from urllib.parse import urlparse
from datetime import datetime
import pytz
from collections import OrderedDict
from functools import lru_cache

app = Flask(__name__)
app.secret_key = 'super secret key'

url_dict = OrderedDict()
user_dict = OrderedDict()
admin_users = ['admin']

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if not username or not password:
		return jsonify({'error': 'Username and password required'}), 400
	if username in user_dict:
		return jsonify({'error': 'Username already exists'}), 400
	user_dict[username] = {'password': password, 'urls': OrderedDict()}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if not username or not password:
		return jsonify({'error': 'Username and password required'}), 400
	user = user_dict.get(username)
	if not user or user['password'] != password:
		return jsonify({'error': 'Invalid username or password'}), 400
	session['username'] = username
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	username = session.get('username')
	if not username:
		return jsonify({'error': 'Not logged in'}), 401
	url = request.json.get('url')
	expiration = request.json.get('expiration')
	if not url:
		return jsonify({'error': 'No url provided'}), 400
	if not urlparse(url).scheme:
		return jsonify({'error': 'Invalid url'}), 400
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	while short_url in url_dict:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
	url_dict[short_url] = {'url': url, 'accesses': [], 'expiration': expiration}
	user_dict[username]['urls'][short_url] = url_dict[short_url]
	return jsonify({'short_url': short_url}), 200

@lru_cache(maxsize=100)
@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url_data = url_dict.get(short_url)
	if not url_data:
		abort(404)
	expiration = url_data.get('expiration')
	if expiration and datetime.now(pytz.utc) > datetime.fromisoformat(expiration):
		abort(410)
	access_time = datetime.now(pytz.utc).isoformat()
	access_location = request.headers.get('X-Forwarded-For', request.remote_addr)
	url_data['accesses'].append({'time': access_time, 'location': access_location})
	return redirect(url_data['url'], code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def analytics(short_url):
	username = session.get('username')
	if not username:
		return jsonify({'error': 'Not logged in'}), 401
	url_data = user_dict[username]['urls'].get(short_url)
	if not url_data:
		abort(404)
	return jsonify(url_data['accesses'])

@app.route('/admin', methods=['GET'])
def admin():
	username = session.get('username')
	if not username or username not in admin_users:
		return jsonify({'error': 'Unauthorized'}), 401
	return jsonify({'users': dict(user_dict), 'urls': dict(url_dict)}), 200

@app.route('/admin/delete_url', methods=['POST'])
def delete_url():
	username = session.get('username')
	if not username or username not in admin_users:
		return jsonify({'error': 'Unauthorized'}), 401
	short_url = request.json.get('short_url')
	if not short_url or short_url not in url_dict:
		return jsonify({'error': 'Invalid url'}), 400
	del url_dict[short_url]
	for user in user_dict.values():
		user['urls'].pop(short_url, None)
	return jsonify({'message': 'URL deleted successfully'}), 200

@app.route('/admin/delete_user', methods=['POST'])
def delete_user():
	username = session.get('username')
	if not username or username not in admin_users:
		return jsonify({'error': 'Unauthorized'}), 401
	user_to_delete = request.json.get('user')
	if not user_to_delete or user_to_delete not in user_dict:
		return jsonify({'error': 'Invalid user'}), 400
	del user_dict[user_to_delete]
	return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
