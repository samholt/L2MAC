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
	url = urls_db.get(short_url, '')
	if url:
		return redirect(url)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	password = request.json['password']
	if username in users_db:
		return {'error': 'Username already exists'}, 400
	else:
		user = User(username, password, {})
		users_db[username] = user
		return {'message': 'User created successfully'}, 201

if __name__ == '__main__':
	app.run(debug=True)
