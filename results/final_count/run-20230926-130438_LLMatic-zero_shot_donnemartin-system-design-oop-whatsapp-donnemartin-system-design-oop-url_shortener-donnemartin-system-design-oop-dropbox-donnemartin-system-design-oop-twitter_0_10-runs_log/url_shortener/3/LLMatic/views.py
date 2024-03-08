from flask import Flask, request, jsonify, redirect, session
import models
import utils
import datetime
import random

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if not username or not password:
		return jsonify({'error': 'Missing username or password'}), 400
	user = models.User(username, password)
	utils.save_user(user)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = utils.get_user_by_username(username)
	if user is None or user.password != password:
		return jsonify({'error': 'Invalid username or password'}), 400
	session['username'] = username
	return jsonify({'message': 'User logged in successfully'}), 200

@app.route('/admin_login', methods=['POST'])
def admin_login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username not in utils.admins or password != 'admin':
		return jsonify({'error': 'Invalid username or password'}), 400
	session['username'] = username
	return jsonify({'message': 'Administrator logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	if 'username' in session:
		del session['username']
	return jsonify({'message': 'User logged out successfully'}), 200

@app.route('/dashboard', methods=['GET', 'PUT', 'DELETE'])
def dashboard():
	if 'username' not in session:
		return jsonify({'error': 'User not logged in'}), 400
	user = utils.get_user_by_username(session['username'])
	if request.method == 'GET':
		urls = [{'original_url': url.original_url, 'short_url': url.short_url, 'click_events': len(url.click_events)} for url in user.urls]
		return jsonify(urls), 200
	elif request.method == 'PUT':
		data = request.get_json()
		original_url = data.get('original_url')
		short_url = data.get('short_url')
		for url in user.urls:
			if url.short_url == short_url:
				url.original_url = original_url
				return jsonify({'message': 'URL updated successfully'}), 200
		return jsonify({'error': 'URL not found'}), 400
	elif request.method == 'DELETE':
		data = request.get_json()
		short_url = data.get('short_url')
		for url in user.urls:
			if url.short_url == short_url:
				user.urls.remove(url)
				return jsonify({'message': 'URL deleted successfully'}), 200
		return jsonify({'error': 'URL not found'}), 400

@app.route('/admin_dashboard', methods=['GET', 'PUT', 'DELETE'])
def admin_dashboard():
	if 'username' not in session or not utils.is_admin(session['username']):
		return jsonify({'error': 'User not logged in or not an administrator'}), 400
	if request.method == 'GET':
		users = utils.get_all_users()
		data = [{'username': user.username, 'urls': [{'original_url': url.original_url, 'short_url': url.short_url, 'click_events': len(url.click_events)} for url in user.urls]} for user in users]
		return jsonify(data), 200
	elif request.method == 'PUT':
		data = request.get_json()
		username = data.get('username')
		original_url = data.get('original_url')
		short_url = data.get('short_url')
		user = utils.get_user_by_username(username)
		if user is None:
			return jsonify({'error': 'User not found'}), 400
		for url in user.urls:
			if url.short_url == short_url:
				url.original_url = original_url
				return jsonify({'message': 'URL updated successfully'}), 200
		return jsonify({'error': 'URL not found'}), 400
	elif request.method == 'DELETE':
		data = request.get_json()
		username = data.get('username')
		short_url = data.get('short_url')
		user = utils.get_user_by_username(username)
		if user is None:
			return jsonify({'error': 'User not found'}), 400
		if short_url is None:
			utils.delete_user(user)
			return jsonify({'message': 'User deleted successfully'}), 200
		for url in user.urls:
			if url.short_url == short_url:
				user.urls.remove(url)
				return jsonify({'message': 'URL deleted successfully'}), 200
		return jsonify({'error': 'URL not found'}), 400

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	for user in utils.get_all_users():
		for url in user.urls:
			if url.short_url == short_url:
				if url.expiration_date and url.expiration_date < datetime.datetime.now():
					return jsonify({'error': 'URL has expired'}), 400
				else:
					return redirect(url.original_url)
	return jsonify({'error': 'URL not found'}), 400
