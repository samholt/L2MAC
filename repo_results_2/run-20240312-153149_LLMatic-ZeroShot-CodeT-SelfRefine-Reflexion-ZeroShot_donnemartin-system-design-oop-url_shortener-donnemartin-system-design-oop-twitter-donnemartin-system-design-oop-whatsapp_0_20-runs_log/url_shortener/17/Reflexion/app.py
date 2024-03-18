from flask import Flask, request, redirect
from dataclasses import dataclass
import random
import string
import datetime
from geolite2 import geolite2

app = Flask(__name__)

# Mock database
urls_db = {}
users_db = {}

@dataclass
class URL:
	original: str
	short: str
	user: str
	clicks: int
	click_data: list

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	user = data.get('user')
	url = URL(original=original_url, short=short_url, user=user, clicks=0, click_data=[])
	urls_db[short_url] = url
	if user:
		users_db[user].urls.append(url)
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls_db.get(short_url)
	if url:
		url.clicks += 1
		url.click_data.append({'time': datetime.datetime.now(), 'location': get_location(request.remote_addr)})
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found'}, 404

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	user = User(username=username, password=password, urls=[])
	users_db[username] = user
	return {'message': 'User created successfully'}

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = users_db.get(username)
	if user:
		return {'username': user.username, 'urls': [url.short for url in user.urls]}
	else:
		return {'error': 'User not found'}, 404

@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
	user = users_db.get(username)
	if user:
		del users_db[username]
		return {'message': 'User deleted successfully'}
	else:
		return {'error': 'User not found'}, 404

@app.route('/url/<short_url>', methods=['GET'])
def get_url(short_url):
	url = urls_db.get(short_url)
	if url:
		return {'original': url.original, 'short': url.short, 'clicks': url.clicks, 'click_data': url.click_data}
	else:
		return {'error': 'URL not found'}, 404

@app.route('/url/<short_url>', methods=['DELETE'])
def delete_url(short_url):
	url = urls_db.get(short_url)
	if url:
		del urls_db[short_url]
		return {'message': 'URL deleted successfully'}
	else:
		return {'error': 'URL not found'}, 404

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	return {'users': list(users_db.keys()), 'urls': list(urls_db.keys())}

@app.route('/admin/user/<username>', methods=['DELETE'])
def admin_delete_user(username):
	user = users_db.get(username)
	if user:
		del users_db[username]
		return {'message': 'User deleted successfully'}
	else:
		return {'error': 'User not found'}, 404

@app.route('/admin/url/<short_url>', methods=['DELETE'])
def admin_delete_url(short_url):
	url = urls_db.get(short_url)
	if url:
		del urls_db[short_url]
		return {'message': 'URL deleted successfully'}
	else:
		return {'error': 'URL not found'}, 404

@app.route('/url/<short_url>/expire', methods=['POST'])
def set_url_expiry(short_url):
	data = request.get_json()
	expiry_date = data['expiry_date']
	url = urls_db.get(short_url)
	if url:
		url.expiry_date = expiry_date
		return {'message': 'Expiry date set successfully'}
	else:
		return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
