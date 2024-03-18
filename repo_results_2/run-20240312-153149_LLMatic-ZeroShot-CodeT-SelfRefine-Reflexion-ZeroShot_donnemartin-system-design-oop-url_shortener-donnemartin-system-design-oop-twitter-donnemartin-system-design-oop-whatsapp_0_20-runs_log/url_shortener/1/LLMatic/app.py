from flask import Flask, redirect, url_for, request, jsonify
from shortener import Shortener
from user import User
from admin import Admin

app = Flask(__name__)
shortener = Shortener()
users_db = {}

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_alias = data.get('custom_alias')
	expiration_date = data.get('expiration_date')
	short_url = shortener.generate_short_url(url, custom_alias, expiration_date)
	if short_url is None:
		return jsonify({'error': 'Invalid URL or alias already in use'}), 400
	return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_to_url(short_url):
	ip_address = request.remote_addr
	url = shortener.get_original_url(short_url, ip_address)
	if url is None:
		return jsonify({'error': 'URL not found or expired'}), 404
	return redirect(url)

@app.route('/analytics/<short_url>')
def view_analytics(short_url):
	analytics = shortener.get_analytics(short_url)
	if analytics is None:
		return jsonify({'error': 'Analytics not found'}), 404
	return jsonify(analytics)

@app.route('/user/create', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = User(username, password)
	message = user.create_account(users_db)
	if 'error' in message:
		return jsonify(message), 400
	return jsonify({'message': message})

@app.route('/admin/create', methods=['POST'])
def create_admin():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	admin = Admin(username, password)
	message = admin.create_account(users_db)
	if 'error' in message:
		return jsonify(message), 400
	return jsonify({'message': message})

if __name__ == '__main__':
	app.run(debug=True)
