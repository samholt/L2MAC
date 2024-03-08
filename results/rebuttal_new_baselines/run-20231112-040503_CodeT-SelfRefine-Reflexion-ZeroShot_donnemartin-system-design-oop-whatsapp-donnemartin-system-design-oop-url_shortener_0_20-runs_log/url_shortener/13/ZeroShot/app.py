from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
import datetime
import random
import string

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'urls': {}
}

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
	expiration: datetime.datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in DB['users']:
		return jsonify({'error': 'User already exists'}), 400
	DB['users'][username] = User(username, password, {})
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	original_url = data.get('original_url')
	short_url = data.get('short_url')
	expiration = data.get('expiration')
	if username not in DB['users'] or DB['users'][username].password != password:
		return jsonify({'error': 'Invalid credentials'}), 401
	if short_url in DB['urls']:
		return jsonify({'error': 'Short URL already exists'}), 400
	DB['urls'][short_url] = URL(original_url, short_url, username, 0, [], datetime.datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S'))
	DB['users'][username].urls[short_url] = DB['urls'][short_url]
	return jsonify({'message': 'URL created successfully'}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url not in DB['urls'] or datetime.datetime.now() > DB['urls'][short_url].expiration:
		return jsonify({'error': 'URL not found or expired'}), 404
	DB['urls'][short_url].clicks += 1
	DB['urls'][short_url].click_data.append(str(datetime.datetime.now()))
	return redirect(DB['urls'][short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username not in DB['users'] or DB['users'][username].password != password:
		return jsonify({'error': 'Invalid credentials'}), 401
	return jsonify({url: {'clicks': DB['users'][username].urls[url].clicks, 'click_data': DB['users'][username].urls[url].click_data} for url in DB['users'][username].urls}), 200

if __name__ == '__main__':
	app.run(debug=True)
