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
	short_url = data.get('short_url')
	username = data.get('username')
	expiration = data.get('expiration')
	if short_url and short_url in urls:
		return jsonify({'message': 'Short URL already exists'}), 400
	if not short_url:
		short_url = generate_short_url()
	if username and username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	if not is_valid_url(original_url):
		return jsonify({'message': 'Invalid URL'}), 400
	url = URL(original_url, short_url, username, 0, [], expiration)
	urls[short_url] = url
	if username:
		users[username].urls[short_url] = url
	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls.get(short_url)
	if not url or (url.expiration and url.expiration < datetime.now()):
		return jsonify({'message': 'URL does not exist or has expired'}), 404
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.now().isoformat()})
	return redirect(url.original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	username = data.get('username')
	if username and username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	if username:
		return jsonify({short_url: url.__dict__ for short_url, url in users[username].urls.items()}), 200
	return jsonify({short_url: url.__dict__ for short_url, url in urls.items()}), 200

@app.route('/delete_url', methods=['DELETE'])
def delete_url():
	data = request.get_json()
	short_url = data['short_url']
	username = data.get('username')
	if short_url not in urls:
		return jsonify({'message': 'URL does not exist'}), 400
	if username and username not in users:
		return jsonify({'message': 'User does not exist'}), 400
	if username and urls[short_url].user != username:
		return jsonify({'message': 'User does not own this URL'}), 403
	delete_url(short_url)
	return jsonify({'message': 'URL deleted successfully'}), 200


# Helper functions
def generate_short_url():
	return str(len(urls) + 1)

def is_valid_url(url):
	try:
		response = requests.get(url)
		return response.status_code == 200
	except:
		return False

def delete_url(short_url):
	user = urls[short_url].user
	if user:
		del users[user].urls[short_url]
	del urls[short_url]

if __name__ == '__main__':
	app.run(debug=True)
