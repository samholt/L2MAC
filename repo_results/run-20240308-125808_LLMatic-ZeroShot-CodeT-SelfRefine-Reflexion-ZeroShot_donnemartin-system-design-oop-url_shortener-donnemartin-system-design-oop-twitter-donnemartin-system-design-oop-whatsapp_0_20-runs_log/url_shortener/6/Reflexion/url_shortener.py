from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls_db = {}
users_db = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	creation_date: datetime.datetime
	expiration_date: datetime.datetime
	clicks: int
	user_id: str

@dataclass
class User:
	user_id: str
	urls: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	user_id = data['user_id']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url, short_url, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=30), 0, user_id)
	urls_db[short_url] = url
	if user_id in users_db:
		users_db[user_id].urls.append(url)
	else:
		user = User(user_id, [url])
		users_db[user_id] = user
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	if short_url in urls_db and urls_db[short_url].expiration_date > datetime.datetime.now():
		urls_db[short_url].clicks += 1
		return redirect(urls_db[short_url].original_url, code=302)
	else:
		return 'URL not found or expired', 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user_id = data['user_id']
	if user_id in users_db:
		user_urls = users_db[user_id].urls
		analytics = [{'original_url': url.original_url, 'short_url': url.short_url, 'clicks': url.clicks, 'creation_date': url.creation_date, 'expiration_date': url.expiration_date} for url in user_urls]
		return jsonify(analytics), 200
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
