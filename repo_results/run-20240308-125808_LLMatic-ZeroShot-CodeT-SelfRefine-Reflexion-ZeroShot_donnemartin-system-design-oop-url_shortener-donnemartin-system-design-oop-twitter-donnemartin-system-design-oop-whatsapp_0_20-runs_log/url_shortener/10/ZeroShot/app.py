from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	id: str
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	id: str
	original_url: str
	short_url: str
	user_id: str
	clicks: list
	expiration_date: datetime

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user_id = str(uuid.uuid4())
	new_user = User(id=user_id, username=data['username'], password=data['password'], urls={})
	users[user_id] = new_user
	return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'message': 'Logged in successfully', 'user_id': user.id}), 200
	return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	url_id = str(uuid.uuid4())
	short_url = f'http://short.ly/{url_id}'
	new_url = URL(id=url_id, original_url=data['original_url'], short_url=short_url, user_id=data['user_id'], clicks=[], expiration_date=data.get('expiration_date'))
	urls[url_id] = new_url
	users[data['user_id']].urls[url_id] = new_url
	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 201

@app.route('/<url_id>', methods=['GET'])
def redirect_url(url_id):
	url = urls.get(url_id)
	if url and (not url.expiration_date or url.expiration_date > datetime.now()):
		url.clicks.append({'click_time': datetime.now().isoformat()})
		return redirect(url.original_url, code=302)
	return jsonify({'message': 'URL not found or expired'}), 404

@app.route('/analytics/<url_id>', methods=['GET'])
def get_analytics(url_id):
	url = urls.get(url_id)
	if url:
		return jsonify({'clicks': url.clicks}), 200
	return jsonify({'message': 'URL not found'}), 404

@app.route('/user_urls/<user_id>', methods=['GET'])
def get_user_urls(user_id):
	user = users.get(user_id)
	if user:
		return jsonify({'urls': [url.short_url for url in user.urls.values()]}), 200
	return jsonify({'message': 'User not found'}), 404

@app.route('/delete_url/<url_id>', methods=['DELETE'])
def delete_url(url_id):
	url = urls.get(url_id)
	if url:
		del urls[url_id]
		del users[url.user_id].urls[url_id]
		return jsonify({'message': 'URL deleted successfully'}), 200
	return jsonify({'message': 'URL not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
