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

@dataclass
class URL:
	original_url: str
	short_url: str
	clicks: int

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	original_url = request.json['original_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = URL(original_url, short_url, 0)
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls_db:
		urls_db[short_url].clicks += 1
		return redirect(urls_db[short_url].original_url)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url in urls_db:
		return {'original_url': urls_db[short_url].original_url, 'clicks': urls_db[short_url].clicks}
	else:
		return {'error': 'URL not found'}, 404

@app.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	password = request.json['password']
	if username in users_db:
		return {'error': 'Username already exists'}, 400
	else:
		users_db[username] = User(username, password, {})
		return {'message': 'User registered successfully'}

@app.route('/login', methods=['POST'])
def login():
	username = request.json['username']
	password = request.json['password']
	if username in users_db and users_db[username].password == password:
		return {'message': 'Login successful'}
	else:
		return {'error': 'Invalid username or password'}, 400

if __name__ == '__main__':
	app.run(debug=True)
