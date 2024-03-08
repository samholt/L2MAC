from flask import Flask, request, redirect
from dataclasses import dataclass
import datetime

app = Flask(__name__)

# Mock database
urls_db = {}
users_db = {}

@dataclass
class User:
	username: str
	password: str

@dataclass
class URL:
	original_url: str
	short_url: str
	user: User
	expiration_date: datetime.datetime

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['username'], data['password'])
	users_db[user.username] = user
	return {'message': 'User registered successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['username'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid username or password'}, 401

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	user = users_db.get(data['username'])
	if not user:
		return {'message': 'User not found'}, 404
	url = URL(data['original_url'], data['short_url'], user, data['expiration_date'])
	urls_db[url.short_url] = url
	return {'message': 'URL shortened successfully'}, 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls_db.get(short_url)
	if not url or url.expiration_date < datetime.datetime.now():
		return {'message': 'URL not found or expired'}, 404
	return redirect(url.original_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
