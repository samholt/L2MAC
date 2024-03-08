from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import requests

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
	clicks: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[username] = User(username, password, {})
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	username = data['username']
	password = data['password']
	original_url = data['original_url']
	short_url = data.get('short_url', None)
	expiration_date = data.get('expiration_date', None)
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	if short_url and short_url in urls:
		return jsonify({'message': 'Short URL already exists'}), 400
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'message': 'Invalid original URL'}), 400
	except:
		return jsonify({'message': 'Invalid original URL'}), 400
	if not short_url:
		short_url = ''.join([chr(i) for i in range(97, 123)])[:5]
	urls[short_url] = URL(original_url, short_url, username, [], expiration_date)
	users[username].urls[short_url] = urls[short_url]
	return jsonify({'message': 'URL created successfully', 'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url not in urls or (urls[short_url].expiration_date and urls[short_url].expiration_date < datetime.now()):
		return jsonify({'message': 'URL not found or expired'}), 404
	urls[short_url].clicks.append({'timestamp': datetime.now().isoformat()})
	return redirect(urls[short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	user_urls = users[username].urls
	analytics = {url.short_url: {'clicks': len(url.clicks), 'last_clicked': max(url.clicks, key=lambda x: x['timestamp'])['timestamp'] if url.clicks else None} for url in user_urls.values()}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
