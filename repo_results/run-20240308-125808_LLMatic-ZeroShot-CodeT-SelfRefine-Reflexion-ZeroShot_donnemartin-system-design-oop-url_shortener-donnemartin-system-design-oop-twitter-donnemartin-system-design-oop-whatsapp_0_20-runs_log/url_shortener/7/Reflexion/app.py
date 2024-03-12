from flask import Flask, request, redirect
from dataclasses import dataclass
import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	original_url: str
	short_url: str
	expiration_date: datetime.datetime
	clicks: int

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	expiration_date = datetime.datetime.now() + datetime.timedelta(days=30)
	urls[short_url] = URL(original_url, short_url, expiration_date, 0)
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls.get(short_url)
	if url and url.expiration_date > datetime.datetime.now():
		url.clicks += 1
		return redirect(url.original_url, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in users:
		return {'error': 'Username already exists'}, 400
	else:
		users[username] = User(username, password, {})
		return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = users.get(username)
	if user and user.password == password:
		return {'message': 'Logged in successfully'}, 200
	else:
		return {'error': 'Invalid username or password'}, 400

if __name__ == '__main__':
	app.run(debug=True)
