from flask import Flask, request, jsonify, redirect
from shortener import Shortener
from analytics import Analytics
from user import User
from admin import Admin

app = Flask(__name__)
shortener = Shortener()
analytics = Analytics()
user = User()
admin = Admin(shortener, user)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if user.register(username, password):
		return jsonify({'message': 'User registered successfully'}), 201
	else:
		return jsonify({'message': 'User already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if user.authenticate(username, password):
		return jsonify({'message': 'User authenticated successfully'}), 200
	else:
		return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_alias = data.get('custom_alias')
	expiry_time = data.get('expiry_time')
	short_url = shortener.generate_short_url(url, custom_alias, expiry_time)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>')
def redirect_to_url(short_url):
	url = shortener.get_original_url(short_url)
	if url is not None:
		analytics.track_click(short_url, request.remote_addr)
		return redirect(url)
	else:
		return 'URL not found', 404

@app.route('/analytics/<short_url>')
def view_analytics(short_url):
	data = analytics.get_click_data(short_url)
	return jsonify(data), 200

@app.route('/admin')
def admin_dashboard():
	data = admin.monitor_system()
	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True)
