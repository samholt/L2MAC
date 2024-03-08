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
	clicks: int
	click_data: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user_id = str(uuid.uuid4())
	user = User(user_id, data['username'], data['password'], {})
	users[user_id] = user
	return jsonify({'user_id': user_id}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	url_id = str(uuid.uuid4())
	url = URL(url_id, data['original_url'], data['short_url'], data['user_id'], 0, [], data['expiration_date'])
	urls[url_id] = url
	users[data['user_id']].urls[url_id] = url
	return jsonify({'url_id': url_id}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	for url in urls.values():
		if url.short_url == short_url:
			url.clicks += 1
			url.click_data.append({'click_time': datetime.now().isoformat()})
			return redirect(url.original_url, code=302)
	return 'URL not found', 404

@app.route('/user/<user_id>/urls', methods=['GET'])
def get_user_urls(user_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	return jsonify({url.id: url.original_url for url in user.urls.values()}), 200

@app.route('/user/<user_id>/url/<url_id>', methods=['DELETE'])
def delete_url(user_id, url_id):
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	url = user.urls.get(url_id)
	if not url:
		return 'URL not found', 404
	del user.urls[url_id]
	del urls[url_id]
	return '', 204

if __name__ == '__main__':
	app.run(debug=True)
