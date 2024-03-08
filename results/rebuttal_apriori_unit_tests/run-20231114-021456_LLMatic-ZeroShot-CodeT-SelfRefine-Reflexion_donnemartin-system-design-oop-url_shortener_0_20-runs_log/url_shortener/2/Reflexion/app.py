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
class URL:
	original: str
	short: str
	user: str
	clicks: int
	created_at: datetime.datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	username = data.get('username')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original=original_url, short=short_url, user=username, clicks=0, created_at=datetime.datetime.now())
	urls[short_url] = url
	if username:
		users[username].urls.append(url)
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url:
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username=username, password=password, urls=[])
	users[username] = user
	return {'message': 'User created'}, 201

if __name__ == '__main__':
	app.run(debug=True)
