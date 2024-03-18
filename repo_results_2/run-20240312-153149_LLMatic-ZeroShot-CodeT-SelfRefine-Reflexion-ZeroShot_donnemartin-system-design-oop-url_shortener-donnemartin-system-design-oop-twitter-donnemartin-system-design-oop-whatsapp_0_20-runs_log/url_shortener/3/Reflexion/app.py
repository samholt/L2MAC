from flask import Flask, request, redirect
from dataclasses import dataclass
import datetime
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
	expiration_date: datetime.datetime
	clicks: int
	click_data: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	expiration_date = datetime.datetime.now() + datetime.timedelta(days=30)
	url = URL(original_url, short_url, expiration_date, 0, [])
	urls_db[short_url] = url
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls_db.get(short_url)
	if url and url.expiration_date > datetime.datetime.now():
		url.clicks += 1
		url.click_data.append({'click_time': datetime.datetime.now()})
		return redirect(url.original_url)
	else:
		return {'error': 'URL expired or does not exist'}

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username, password, {})
	users_db[username] = user
	return {'message': 'User created successfully'}

@app.route('/user/<username>/urls', methods=['GET'])
def get_user_urls(username):
	user = users_db.get(username)
	if user:
		return {'urls': user.urls}
	else:
		return {'error': 'User does not exist'}

@app.route('/user/<username>/url/<short_url>', methods=['DELETE'])
def delete_user_url(username, short_url):
	user = users_db.get(username)
	if user and short_url in user.urls:
		del user.urls[short_url]
		return {'message': 'URL deleted successfully'}
	else:
		return {'error': 'URL does not exist'}

if __name__ == '__main__':
	app.run(debug=True)
