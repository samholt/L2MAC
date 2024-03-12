from flask import Flask, request, redirect
from dataclasses import dataclass
import datetime
import random
import string
import hashlib

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
	expiration: datetime.datetime

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if username in users:
		return {'message': 'Username already exists'}, 400
	users[username] = User(username, password, {})
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = hashlib.sha256(data['password'].encode()).hexdigest()
	if username not in users or users[username].password != password:
		return {'message': 'Invalid username or password'}, 400
	return {'message': 'Logged in successfully'}, 200

@app.route('/shorten', methods=['POST'])
def shorten():
	data = request.get_json()
	original_url = data['original_url']
	username = data.get('username')
	short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	while short_url in urls:
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	expiration = data.get('expiration')
	if expiration:
		expiration = datetime.datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S')
	url = URL(original_url, short_url, username, 0, [], expiration)
	urls[short_url] = url
	if username:
		users[username].urls[short_url] = url
	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	if short_url not in urls:
		return {'message': 'URL not found'}, 404
	if urls[short_url].expiration and urls[short_url].expiration < datetime.datetime.now():
		return {'message': 'URL has expired'}, 410
	urls[short_url].clicks += 1
	urls[short_url].click_data.append({'time': datetime.datetime.now().isoformat()})
	return redirect(urls[short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def analytics():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return {'message': 'User not found'}, 404
	user_urls = users[username].urls
	analytics_data = {}
	for short_url, url in user_urls.items():
		analytics_data[short_url] = {'clicks': url.clicks, 'click_data': url.click_data}
	return analytics_data, 200

if __name__ == '__main__':
	app.run(debug=True)
