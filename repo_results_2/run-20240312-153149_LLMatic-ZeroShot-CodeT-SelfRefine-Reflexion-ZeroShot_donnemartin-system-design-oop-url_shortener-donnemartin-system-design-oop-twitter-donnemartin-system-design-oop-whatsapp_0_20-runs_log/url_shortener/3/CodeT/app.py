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
	user = User(id=user_id, username=data['username'], password=data['password'], urls={})
	users[user_id] = user
	return jsonify({'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.username == data['username'] and user.password == data['password']:
			return jsonify({'user_id': user.id}), 200
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/shorten', methods=['POST'])
def shorten():
	data = request.get_json()
	url_id = str(uuid.uuid4())
	short_url = f'http://short.ly/{url_id}'
	url = URL(id=url_id, original_url=data['original_url'], short_url=short_url, user_id=data['user_id'], clicks=[], expiration_date=data.get('expiration_date'))
	urls[url_id] = url
	users[data['user_id']].urls[url_id] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<url_id>', methods=['GET'])
def redirect_to_original(url_id):
	url = urls.get(url_id)
	if url and (not url.expiration_date or url.expiration_date > datetime.now()):
		url.clicks.append({'timestamp': datetime.now().isoformat()})
		return redirect(url.original_url, code=302)
	return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics/<url_id>', methods=['GET'])
def analytics(url_id):
	url = urls.get(url_id)
	if url:
		return jsonify({'clicks': url.clicks}), 200
	return jsonify({'error': 'URL not found'}), 404

@app.route('/user/<user_id>', methods=['GET'])
def user_urls(user_id):
	user = users.get(user_id)
	if user:
		return jsonify({'urls': [url.short_url for url in user.urls.values()]}), 200
	return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
