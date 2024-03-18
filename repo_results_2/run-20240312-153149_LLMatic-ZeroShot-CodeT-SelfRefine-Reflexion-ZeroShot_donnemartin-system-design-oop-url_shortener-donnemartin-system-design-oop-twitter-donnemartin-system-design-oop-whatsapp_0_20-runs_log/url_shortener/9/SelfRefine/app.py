from flask import Flask, request, redirect
from dataclasses import dataclass
import requests
from datetime import datetime
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
	clicks: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	original_url = request.json['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[short_url] = URL(original_url, short_url, [], datetime.now())
	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls:
		return redirect(urls[short_url].original_url)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	return {'analytics': {url: len(urls[url].clicks) for url in urls}}, 200

@app.route('/user', methods=['POST'])
def create_user():
	username = request.json['username']
	password = request.json['password']
	users[username] = User(username, password, {})
	return {'message': 'User created'}, 200

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(username):
	if username in users:
		if request.method == 'GET':
			return {'user': vars(users[username])}, 200
		elif request.method == 'PUT':
			new_password = request.json['password']
			users[username].password = new_password
			return {'message': 'Password updated'}, 200
		elif request.method == 'DELETE':
			del users[username]
			return {'message': 'User deleted'}, 200
	else:
		return {'error': 'User not found'}, 404

@app.route('/admin', methods=['GET', 'DELETE'])
def admin_dashboard():
	if request.method == 'GET':
		return {'users': {user: vars(users[user]) for user in users}}, 200
	elif request.method == 'DELETE':
		users.clear()
		return {'message': 'All users deleted'}, 200

if __name__ == '__main__':
	app.run(debug=True)
