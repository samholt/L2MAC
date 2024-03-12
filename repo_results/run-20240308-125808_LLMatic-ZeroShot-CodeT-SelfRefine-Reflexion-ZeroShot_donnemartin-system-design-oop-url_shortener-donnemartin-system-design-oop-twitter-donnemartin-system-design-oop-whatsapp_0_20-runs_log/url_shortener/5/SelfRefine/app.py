from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests
import string
import random

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	original_url: str
	short_url: str
	user: str
	clicks: int
	click_data: list
	expiration: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password, {})
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = data['short_url']
	username = data['username']
	password = data['password']
	expiration = datetime.strptime(data['expiration'], '%Y-%m-%d %H:%M:%S')
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	if short_url in urls:
		short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'message': 'Invalid URL'}), 400
	except:
		return jsonify({'message': 'Invalid URL'}), 400
	urls[short_url] = URL(original_url, short_url, username, 0, [], expiration)
	users[username].urls[short_url] = urls[short_url]
	return jsonify({'message': 'URL created successfully', 'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url not in urls:
		return jsonify({'message': 'URL does not exist'}), 404
	url = urls[short_url]
	if datetime.now() > url.expiration:
		return jsonify({'message': 'URL has expired'}), 410
	url.clicks += 1
	url.click_data.append({'click_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
	return redirect(url.original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	user = users[username]
	analytics = {}
	for short_url, url in user.urls.items():
		analytics[short_url] = {'clicks': url.clicks, 'click_data': url.click_data}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
