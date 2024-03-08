from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime, timedelta
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
	original: str
	shortened: str
	clicks: int
	click_dates: list
	click_geolocations: list
	expiration_time: datetime

@app.route('/shorten', methods=['POST'])
def shorten():
	original_url = request.json['url']
	shortened_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	urls[shortened_url] = URL(original_url, shortened_url, 0, [], [], datetime.now() + timedelta(days=30))
	return {'shortened_url': shortened_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	if short_url in urls:
		url = urls[short_url]
		url.clicks += 1
		url.click_dates.append(datetime.now())
		return redirect(url.original), 302
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics', methods=['GET'])
def analytics():
	return {url.shortened: url.clicks for url in urls.values()}

@app.route('/user', methods=['POST'])
def create_user():
	username = request.json['username']
	password = request.json['password']
	users[username] = User(username, password, {})
	return {'message': 'User created'}, 201

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(username):
	if username in users:
		if request.method == 'GET':
			return users[username].urls
		elif request.method == 'PUT':
			users[username].password = request.json['password']
			return {'message': 'Password updated'}, 200
		elif request.method == 'DELETE':
			del users[username]
			return {'message': 'User deleted'}, 200
	else:
		return {'error': 'User not found'}, 404

@app.route('/admin', methods=['POST'])
def create_admin():
	# TODO: Implement admin account creation
	pass

@app.route('/admin/<username>', methods=['GET', 'DELETE'])
def manage_admin(username):
	# TODO: Implement admin account management
	pass

if __name__ == '__main__':
	app.run(debug=True)
