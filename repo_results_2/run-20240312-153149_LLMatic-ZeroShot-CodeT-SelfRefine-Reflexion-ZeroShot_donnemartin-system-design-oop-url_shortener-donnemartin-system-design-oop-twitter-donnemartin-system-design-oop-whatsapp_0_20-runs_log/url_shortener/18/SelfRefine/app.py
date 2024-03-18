from flask import Flask, request, redirect
from dataclasses import dataclass
import requests
from datetime import datetime

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
	expiration: datetime

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if username in users:
		return {'message': 'Username already exists'}, 400
	users[username] = User(username, password, {})
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if username not in users or users[username].password != password:
		return {'message': 'Invalid username or password'}, 400
	return {'message': 'Logged in successfully'}, 200

@app.route('/shorten', methods=['POST'])
def shorten():
	original_url = request.json.get('original_url')
	short_url = request.json.get('short_url')
	username = request.json.get('username')
	expiration = request.json.get('expiration')
	if not original_url or not short_url or not username:
		return {'message': 'Missing required fields'}, 400
	if short_url in urls:
		return {'message': 'Short URL already exists'}, 400
	if username not in users:
		return {'message': 'User does not exist'}, 400
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return {'message': 'Invalid original URL'}, 400
	except:
		return {'message': 'Invalid original URL'}, 400
	urls[short_url] = URL(original_url, short_url, username, [], expiration)
	users[username].urls[short_url] = urls[short_url]
	return {'message': 'URL shortened successfully'}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
	if short_url not in urls:
		return {'message': 'URL does not exist'}, 404
	if urls[short_url].expiration and urls[short_url].expiration < datetime.now():
		return {'message': 'URL has expired'}, 410
	urls[short_url].clicks.append((datetime.now(), request.remote_addr))
	return redirect(urls[short_url].original_url, code=302)

@app.route('/analytics', methods=['GET'])
def analytics():
	username = request.args.get('username')
	if username not in users:
		return {'message': 'User does not exist'}, 400
	user_urls = users[username].urls
	analytics_data = {}
	for short_url, url in user_urls.items():
		click_data = []
		for click in url.clicks:
			click_data.append((click[0], click[1]))
		analytics_data[short_url] = click_data
	return analytics_data, 200

if __name__ == '__main__':
	app.run(debug=True)

