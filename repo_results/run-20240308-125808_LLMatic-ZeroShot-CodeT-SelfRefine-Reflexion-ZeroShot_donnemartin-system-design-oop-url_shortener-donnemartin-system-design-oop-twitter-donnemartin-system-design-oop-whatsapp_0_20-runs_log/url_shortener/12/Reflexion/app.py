from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}
users_db = {}

@dataclass
class User:
	username: str
	password: str
	urls: dict

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	url = request.json['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = url
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls_db.get(short_url)
	if url is not None:
		return redirect(url)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	password = request.json['password']
	user = User(username, password, {})
	users_db[username] = user
	return {'message': 'User registered successfully'}

@app.route('/login', methods=['POST'])
def login():
	username = request.json['username']
	password = request.json['password']
	user = users_db.get(username)
	if user is not None and user.password == password:
		return {'message': 'Login successful'}
	else:
		return {'error': 'Invalid username or password'}, 401

if __name__ == '__main__':
	app.run(debug=True)
