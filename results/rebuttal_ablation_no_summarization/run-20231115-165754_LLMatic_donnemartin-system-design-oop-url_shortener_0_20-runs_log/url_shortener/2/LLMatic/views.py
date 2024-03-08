from flask import Flask, request, session, redirect
from models import User, URL, Click
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'

users = {}
urls = {}
clicks = {}

@app.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	password = request.form['password']
	if username in users:
		return 'Username already exists', 400
	users[username] = User(username, password)
	return 'User created successfully', 200

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username not in users or users[username].password != password:
		return 'Invalid username or password', 400
	session['username'] = username
	return 'Logged in successfully', 200

@app.route('/urls', methods=['GET'])
def get_urls():
	if 'username' not in session:
		return 'Not logged in', 401
	user_urls = [url for url in urls.values() if url.user.username == session['username']]
	return {'urls': [url.original_url for url in user_urls]}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url not in urls:
		return 'URL not found', 404
	url = urls[short_url]
	if url.expiration_date and datetime.now() > url.expiration_date:
		return 'URL expired', 410
	click = Click(url, datetime.now(), request.remote_addr)
	clicks[url.shortened_url] = click
	return redirect(url.original_url, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url not in urls:
		return 'URL not found', 404
	url_clicks = [click for click in clicks.values() if click.url.shortened_url == short_url]
	return {'clicks': [{'datetime': click.datetime, 'location': click.location} for click in url_clicks]}, 200

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	if 'username' not in session or session['username'] != 'admin':
		return 'Unauthorized', 403
	all_users = [user.username for user in users.values()]
	all_urls = [url.shortened_url for url in urls.values()]
	return {'users': all_users, 'urls': all_urls}, 200

@app.route('/admin/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
	if 'username' not in session or session['username'] != 'admin':
		return 'Unauthorized', 403
	if username not in users:
		return 'User not found', 404
	del users[username]
	return 'User deleted successfully', 200

@app.route('/admin/delete_url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
	if 'username' not in session or session['username'] != 'admin':
		return 'Unauthorized', 403
	if short_url not in urls:
		return 'URL not found', 404
	del urls[short_url]
	return 'URL deleted successfully', 200
