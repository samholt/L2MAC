from flask import Flask, redirect, jsonify, request
from url_shortener import short_links_db, generate_short_url, is_url_expired
from user_accounts import UserAccounts
from analytics import track_click, get_statistics

app = Flask(__name__)
user_accounts = UserAccounts()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/<short_url>')
def redirect_to_original(short_url):
	if short_url in short_links_db:
		if is_url_expired(short_url):
			return 'URL expired', 410
		track_click(short_url, request.remote_addr)
		return redirect(short_links_db[short_url]['url'])
	else:
		return 'URL not found', 404

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json.get('url')
	short_url = generate_short_url(url)
	return jsonify({'short_url': short_url})

@app.route('/analytics/<short_url>')
def analytics(short_url):
	return jsonify(get_statistics(short_url))

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if user_accounts.register(username, password):
		return 'Registration successful'
	else:
		return 'Registration failed', 400

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if user_accounts.login(username, password):
		return 'Login successful'
	else:
		return 'Login failed', 400

@app.route('/add_url', methods=['POST'])
def add_url():
	username = request.json.get('username')
	url = request.json.get('url')
	if user_accounts.add_url(username, url):
		return 'URL added successfully'
	else:
		return 'Failed to add URL', 400

@app.route('/get_urls/<username>')
def get_urls(username):
	urls = user_accounts.get_urls(username)
	if urls is not None:
		return jsonify(urls)
	else:
		return 'User not found', 404

@app.route('/admin/dashboard')
def admin_dashboard():
	return jsonify({'users': user_accounts.users, 'short_links': short_links_db})

@app.route('/admin/delete_url/<username>/<url>')
def delete_url(username, url):
	if user_accounts.delete_url(username, url):
		return 'URL deleted successfully'
	else:
		return 'Failed to delete URL', 400

@app.route('/admin/delete_user/<username>')
def delete_user(username):
	if user_accounts.delete_user(username):
		return 'User deleted successfully'
	else:
		return 'Failed to delete user', 400

if __name__ == '__main__':
	app.run(debug=True)
