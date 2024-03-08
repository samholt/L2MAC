from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	created_at: datetime
	expires_at: datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	user = data.get('user')
	expires_at = data.get('expires_at')
	shortened_url = str(uuid.uuid4())[:8]
	url = URL(original_url, shortened_url, user, 0, datetime.now(), expires_at)
	urls[shortened_url] = url
	if user:
		users[user].urls.append(url)
	return {'shortened_url': shortened_url}

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
	url = urls.get(shortened_url)
	if url and (not url.expires_at or url.expires_at > datetime.now()):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username, password, [])
	users[username] = user
	return {'message': 'User registered successfully'}

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users.get(username)
	if user and user.password == password:
		return {'message': 'Login successful'}
	else:
		return {'error': 'Invalid username or password'}, 401

if __name__ == '__main__':
	app.run(debug=True)
