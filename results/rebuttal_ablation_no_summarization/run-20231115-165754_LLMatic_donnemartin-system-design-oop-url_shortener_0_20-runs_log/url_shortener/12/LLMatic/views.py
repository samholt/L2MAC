from flask import Flask, request, redirect, session
from utils import generate_short_url, validate_url, record_click, has_url_expired
from models import User, URL

app = Flask(__name__)
app.secret_key = 'secret'

url_db = {}
click_db = {}
user_db = {}

@app.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	password = request.json['password']
	is_admin = request.json.get('is_admin', False)
	if username in user_db:
		return {'error': 'Username already exists'}, 400
	user_db[username] = User(len(user_db), username, password, is_admin)
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json['username']
	password = request.json['password']
	if username in user_db and user_db[username].password == password:
		session['username'] = username
		return {'message': 'Login successful'}, 200
	return {'error': 'Invalid username or password'}, 400

@app.route('/logout', methods=['POST'])
def logout():
	if 'username' in session:
		del session['username']
	return {'message': 'Logout successful'}, 200

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json['url']
	if validate_url(url):
		short_url = generate_short_url(url)
		url_db[short_url] = URL(len(url_db), url, short_url, session.get('username'), None)
		return {'short_url': short_url}, 200
	else:
		return {'error': 'Invalid URL'}, 400

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url in url_db:
		if has_url_expired(url_db[short_url]):
			return {'error': 'URL has expired'}, 410
		record_click(short_url, request.remote_addr, click_db)
		return redirect(url_db[short_url].original_url, code=302)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/set_expiration/<short_url>', methods=['POST'])
def set_expiration(short_url):
	if 'username' not in session:
		return {'error': 'Not logged in'}, 401
	if short_url not in url_db or url_db[short_url].user_id != session['username']:
		return {'error': 'URL not found'}, 404
	expiration_date = request.json['expiration_date']
	url_db[short_url].expiration_date = expiration_date
	return {'message': 'Expiration date set'}, 200

@app.route('/analytics/<short_url>', methods=['GET'])
def get_url_analytics(short_url):
	if short_url in url_db:
		clicks = click_db.get(short_url, [])
		return {'clicks': clicks}, 200
	else:
		return {'error': 'URL not found'}, 404

@app.route('/my_urls', methods=['GET'])
def get_my_urls():
	if 'username' not in session:
		return {'error': 'Not logged in'}, 401
	urls = [url for url in url_db.values() if url.user_id == session['username']]
	return {'urls': [url.shortened_url for url in urls]}, 200

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	if 'username' not in session or not user_db[session['username']].is_admin:
		return {'error': 'Not authorized'}, 403
	users = [user.username for user in user_db.values()]
	urls = [url.shortened_url for url in url_db.values()]
	return {'users': users, 'urls': urls}, 200

@app.route('/admin/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
	if 'username' not in session or not user_db[session['username']].is_admin:
		return {'error': 'Not authorized'}, 403
	if username in user_db:
		del user_db[username]
		return {'message': 'User deleted'}, 200
	else:
		return {'error': 'User not found'}, 404

@app.route('/admin/delete_url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
	if 'username' not in session or not user_db[session['username']].is_admin:
		return {'error': 'Not authorized'}, 403
	if short_url in url_db:
		del url_db[short_url]
		return {'message': 'URL deleted'}, 200
	else:
		return {'error': 'URL not found'}, 404

