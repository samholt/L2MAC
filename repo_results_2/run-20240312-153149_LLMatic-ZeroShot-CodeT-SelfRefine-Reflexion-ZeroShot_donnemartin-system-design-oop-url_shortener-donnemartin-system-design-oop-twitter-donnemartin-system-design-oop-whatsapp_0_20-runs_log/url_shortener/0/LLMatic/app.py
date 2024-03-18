from flask import Flask, redirect, abort, request
from shortener import Shortener
from datetime import datetime
from models import User, URL

app = Flask(__name__)
shortener = Shortener()
users = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = shortener.urls.get(short_url)
	if url is not None:
		if datetime.now() > url.expirationDate:
			abort(410, 'URL has expired')
		shortener.record_click(short_url, 'mock_location')
		return redirect(url.original_url)
	else:
		abort(404, 'URL not found')

@app.route('/register', methods=['POST'])
def register():
	username = request.form.get('username')
	password = request.form.get('password')
	isAdmin = request.form.get('isAdmin') == 'True'
	if username in users:
		abort(400)
	users[username] = User(username, password, [], isAdmin)
	return 'User registered successfully', 201

@app.route('/login', methods=['POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	user = users.get(username)
	if user is None or user.password != password:
		abort(401)
	return 'User logged in successfully'

@app.route('/admin/users', methods=['GET'])
def get_all_users():
	if not request.form.get('isAdmin') == 'True':
		abort(403)
	return {user.username: user.urls for user in users.values()}

@app.route('/admin/urls', methods=['GET'])
def get_all_urls():
	if not request.form.get('isAdmin') == 'True':
		abort(403)
	return shortener.urls

@app.route('/admin/delete_user', methods=['DELETE'])
def delete_user():
	if not request.form.get('isAdmin') == 'True':
		abort(403)
	username = request.form.get('username')
	if username in users:
		del users[username]
		return 'User deleted successfully'
	else:
		abort(404)

@app.route('/admin/delete_url', methods=['DELETE'])
def delete_url():
	if not request.form.get('isAdmin') == 'True':
		abort(403)
	short_url = request.form.get('short_url')
	if short_url in shortener.urls:
		del shortener.urls[short_url]
		return 'URL deleted successfully'
	else:
		abort(404)

if __name__ == '__main__':
	app.run(debug=True)
