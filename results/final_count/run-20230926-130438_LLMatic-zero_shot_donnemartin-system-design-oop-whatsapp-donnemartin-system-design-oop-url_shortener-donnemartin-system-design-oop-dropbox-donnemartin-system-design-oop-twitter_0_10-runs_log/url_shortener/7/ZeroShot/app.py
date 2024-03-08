from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import pytz
import random
import string

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
		return jsonify({'message': 'Username already exists.'}), 400
	users[username] = User(username, password, {})
	return jsonify({'message': 'User created successfully.'}), 200

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	original_url = data['original_url']
	username = data['username']
	password = data['password']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password.'}), 400
	if 'short_url' in data:
		short_url = data['short_url']
	if short_url in urls:
		return jsonify({'message': 'Short URL already exists.'}), 400
	urls[short_url] = URL(original_url, short_url, username, 0, [], None)
	users[username].urls[short_url] = urls[short_url]
	return jsonify({'message': 'URL created successfully.', 'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url not in urls or (urls[short_url].expiration and urls[short_url].expiration < datetime.now(pytz.UTC)):
		return jsonify({'message': 'URL not found or expired.'}), 404
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'timestamp': datetime.now(pytz.UTC).isoformat()})
	return redirect(urls[short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in users or users[username].password != password:
		return jsonify({'message': 'Invalid username or password.'}), 400
	user_urls = users[username].urls
	analytics = {url: {'clicks': user_urls[url].clicks, 'click_data': user_urls[url].click_data} for url in user_urls}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
