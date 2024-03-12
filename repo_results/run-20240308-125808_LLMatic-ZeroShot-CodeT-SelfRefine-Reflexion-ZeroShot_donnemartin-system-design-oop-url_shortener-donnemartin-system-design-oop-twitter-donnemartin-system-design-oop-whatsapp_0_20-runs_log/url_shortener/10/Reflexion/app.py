from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import pytz
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}
users_db = {}
analytics_db = {}

@dataclass
class User:
	username: str
	password: str
	urls: list

@dataclass
class URL:
	original_url: str
	short_url: str
	expiration_date: datetime

@dataclass
class Analytics:
	url: str
	clicks: int
	click_details: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls_db[short_url] = URL(original_url, short_url, None)
	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls_db:
		return redirect(urls_db[short_url].original_url, code=302)
	else:
		return 'URL not found!', 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	if short_url in analytics_db:
		return jsonify({'clicks': analytics_db[short_url].clicks, 'click_details': analytics_db[short_url].click_details}), 200
	else:
		return 'URL not found!', 404

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data['username']
	password = data['password']
	users_db[username] = User(username, password, [])
	return 'User created successfully!', 200

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	if username in users_db:
		return jsonify({'username': users_db[username].username, 'urls': [url.short_url for url in users_db[username].urls]}), 200
	else:
		return 'User not found!', 404

if __name__ == '__main__':
	app.run(debug=True)
