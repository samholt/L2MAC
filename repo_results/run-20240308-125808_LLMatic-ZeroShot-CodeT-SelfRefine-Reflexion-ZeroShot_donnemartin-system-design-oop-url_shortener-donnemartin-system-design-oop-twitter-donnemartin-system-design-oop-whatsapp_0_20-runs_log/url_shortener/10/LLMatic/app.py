from flask import Flask, redirect, request
from url_shortener import get_original_url, generate_short_url, validate_url, url_db
from user import User
from analytics import get_url_stats, record_click

app = Flask(__name__)

user_db = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	url = get_original_url(short_url)
	if url:
		record_click(short_url, request.remote_addr)
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_alias = data.get('custom_alias')
	expiration = data.get('expiration')
	if not validate_url(url):
		return 'Invalid URL', 400
	short_url = generate_short_url(url, custom_alias, expiration)
	return {'short_url': short_url}, 200

@app.route('/user', methods=['POST', 'PUT', 'DELETE'])
def manage_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if request.method == 'POST':
		user_db[username] = User(username, password)
		return 'User created', 201
	elif request.method == 'PUT':
		user = user_db.get(username)
		if user:
			user.edit_user(username, password)
			return 'User updated', 200
		else:
			return 'User not found', 404
	elif request.method == 'DELETE':
		user = user_db.pop(username, None)
		if user:
			return 'User deleted', 200
		else:
			return 'User not found', 404

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return {
			'users': list(user_db.keys()),
			'urls': list(url_db.keys())
		}
	elif request.method == 'DELETE':
		data = request.get_json()
		if 'user' in data:
			user_db.pop(data['user'], None)
		if 'url' in data:
			url_db.pop(data['url'], None)
		return 'Deleted', 200

@app.route('/admin/<short_url>')
def admin_url_stats(short_url):
	stats = get_url_stats(short_url)
	if stats:
		return stats
	else:
		return 'URL not found', 404

if __name__ == '__main__':
	app.run(debug=True)
