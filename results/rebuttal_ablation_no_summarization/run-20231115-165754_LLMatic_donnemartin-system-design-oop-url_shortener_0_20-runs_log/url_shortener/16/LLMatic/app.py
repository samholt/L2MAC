from flask import Flask, request, jsonify
import hashlib
from datetime import datetime
from collections import Counter

app = Flask(__name__)

users = {}
urls = {}
admins = ['admin']

# Initialize 'admin' user in urls dictionary
urls['admin'] = {}

@app.route('/create_user', methods=['POST'])
def create_user():
	username = request.json.get('username')
	password = request.json.get('password')
	if username in users:
		return jsonify({'error': 'Username already exists'}), 400
	users[username] = hashlib.md5(password.encode()).hexdigest()
	urls[username] = {}
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if username not in users or users[username] != hashlib.md5(password.encode()).hexdigest():
		return jsonify({'error': 'Invalid username or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/<username>/urls', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_urls(username):
	if request.method == 'GET':
		return jsonify(urls[username])
	elif request.method == 'POST':
		short_url = request.json.get('short_url')
		long_url = request.json.get('long_url')
		expiration_date = request.json.get('expiration_date')
		urls[username][short_url] = {'url': long_url, 'access_events': [], 'expiration_date': expiration_date}
		return jsonify({'message': 'URL added successfully'}), 201
	elif request.method == 'PUT':
		short_url = request.json.get('short_url')
		new_long_url = request.json.get('new_long_url')
		if short_url not in urls[username]:
			return jsonify({'error': 'URL not found'}), 404
		urls[username][short_url]['url'] = new_long_url
		return jsonify({'message': 'URL updated successfully'}), 200
	elif request.method == 'DELETE':
		short_url = request.json.get('short_url')
		if short_url not in urls[username]:
			return jsonify({'error': 'URL not found'}), 404
		del urls[username][short_url]
		return jsonify({'message': 'URL deleted successfully'}), 200

@app.route('/<username>/urls/<short_url>/access', methods=['POST'])
def record_access(username, short_url):
	if short_url not in urls[username]:
		return jsonify({'error': 'URL not found'}), 404
	if datetime.now() > datetime.fromisoformat(urls[username][short_url]['expiration_date']):
		return jsonify({'error': 'URL has expired'}), 403
	access_event = {'timestamp': datetime.now().isoformat(), 'location': request.json.get('location')}
	urls[username][short_url]['access_events'].append(access_event)
	return jsonify({'message': 'Access recorded successfully'}), 201

@app.route('/<username>/urls/<short_url>/analytics', methods=['GET'])
def get_analytics(username, short_url):
	if short_url not in urls[username]:
		return jsonify({'error': 'URL not found'}), 404
	return jsonify(urls[username][short_url]['access_events'])

@app.route('/admin/dashboard', methods=['GET', 'DELETE'])
def admin_dashboard():
	admin_username = request.json.get('username')
	if admin_username not in admins:
		return jsonify({'error': 'Access denied'}), 403
	if request.method == 'GET':
		return jsonify({'users': users, 'urls': urls})
	elif request.method == 'DELETE':
		username_to_delete = request.json.get('username_to_delete')
		url_to_delete = request.json.get('url_to_delete')
		if username_to_delete and username_to_delete in users:
			del users[username_to_delete]
			del urls[username_to_delete]
		if url_to_delete:
			for user_urls in urls.values():
				if url_to_delete in user_urls:
					del user_urls[url_to_delete]
		return jsonify({'message': 'Deletion successful'}), 200

@app.route('/admin/analytics', methods=['GET'])
def admin_analytics():
	admin_username = request.json.get('username')
	if admin_username not in admins:
		return jsonify({'error': 'Access denied'}), 403
	total_urls = sum(len(user_urls) for user_urls in urls.values())
	access_counts = Counter(short_url for user_urls in urls.values() for short_url, url_data in user_urls.items() if url_data['access_events'])
	most_accessed_urls = access_counts.most_common(5)
	return jsonify({'total_urls': total_urls, 'most_accessed_urls': most_accessed_urls})

if __name__ == '__main__':
	app.run(debug=True)
