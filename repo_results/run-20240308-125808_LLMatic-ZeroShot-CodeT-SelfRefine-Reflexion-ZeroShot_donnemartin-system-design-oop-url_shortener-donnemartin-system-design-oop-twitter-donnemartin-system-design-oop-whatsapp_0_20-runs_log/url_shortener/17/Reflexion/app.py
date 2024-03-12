from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import pytz

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

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, password, {})
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/shorten', methods=['POST'])
def shorten():
	data = request.get_json()
	original_url = data['original_url']
	short_url = data['short_url']
	username = data['username']
	expiration = datetime.strptime(data['expiration'], '%Y-%m-%dT%H:%M:%S%z')
	if short_url in urls:
		return jsonify({'message': 'Short URL already exists'}), 400
	urls[short_url] = URL(original_url, short_url, username, 0, [], expiration)
	users[username].urls[short_url] = urls[short_url]
	return jsonify({'message': 'URL shortened successfully'}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect(short_url):
	if short_url not in urls or datetime.now(pytz.utc) > urls[short_url].expiration:
		return jsonify({'message': 'URL not found or expired'}), 404
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'timestamp': datetime.now(pytz.utc).isoformat(), 'location': request.remote_addr})
	return redirect(urls[short_url].original_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
