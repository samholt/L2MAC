from flask import Flask, request, jsonify, redirect
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
	clicks: int
	click_data: list
	expiration: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'Username already exists'}), 400
	users[username] = User(username, password, {})
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = data['short_url']
	username = data['username']
	password = data['password']
	expiration = datetime.strptime(data['expiration'], '%Y-%m-%d %H:%M:%S')
	if short_url in urls:
		return jsonify({'message': 'Short URL already exists'}), 400
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except requests.exceptions.RequestException:
		return jsonify({'message': 'Invalid original URL'}), 400
	urls[short_url] = URL(original_url, short_url, username, 0, [], expiration)
	users[username].urls[short_url] = urls[short_url]
	return jsonify({'message': 'URL shortened successfully'}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url not in urls or datetime.now() > urls[short_url].expiration:
		return jsonify({'message': 'Invalid or expired short URL'}), 404
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'time': datetime.now().isoformat()})
	return redirect(urls[short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	username = request.args.get('username')
	password = request.args.get('password')
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 401
	user_urls = users[username].urls
	analytics = {url.short_url: {'clicks': url.clicks, 'click_data': url.click_data} for url in user_urls.values()}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
