from flask import Flask, request, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from dataclasses import dataclass
from datetime import datetime
import string
import random

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# Mock database
users = {}
urls = {}

@dataclass
class User(UserMixin):
	id: str

@login_manager.user_loader
def load_user(user_id):
	return users.get(user_id)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(id=username)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if user is None:
		return jsonify({'message': 'Invalid username or password'}), 401
	login_user(user)
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/shorten', methods=['POST'])
@login_required
def shorten():
	data = request.get_json()
	original_url = data.get('original_url')
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	urls[short_url] = {'original_url': original_url, 'user': current_user.id, 'clicks': [], 'created_at': datetime.now()}
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>')
def redirect_to_original(short_url):
	url_data = urls.get(short_url)
	if url_data is None:
		return jsonify({'message': 'URL not found'}), 404
	url_data['clicks'].append({'timestamp': datetime.now()})
	return redirect(url_data['original_url'])

@app.route('/analytics/<short_url>')
@login_required
def analytics(short_url):
	url_data = urls.get(short_url)
	if url_data is None or url_data['user'] != current_user.id:
		return jsonify({'message': 'URL not found'}), 404
	return jsonify({'clicks': len(url_data['clicks']), 'created_at': url_data['created_at'].isoformat(), 'clicks_data': [{'timestamp': click['timestamp'].isoformat()} for click in url_data['clicks']]}), 200

if __name__ == '__main__':
	app.run(debug=True)
