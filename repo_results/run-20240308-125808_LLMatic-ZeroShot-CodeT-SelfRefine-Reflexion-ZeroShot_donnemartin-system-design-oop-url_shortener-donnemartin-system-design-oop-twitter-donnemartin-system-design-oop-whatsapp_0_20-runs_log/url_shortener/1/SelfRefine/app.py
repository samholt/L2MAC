from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime, timedelta
import random
import string

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'urls': {},
	'clicks': {}
}

@dataclass
class User:
	id: str
	urls: list

@dataclass
class URL:
	id: str
	original_url: str
	short_url: str
	user_id: str
	expiration_date: datetime

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	user_id = data.get('user_id')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	expiration_date = datetime.now() + timedelta(days=30) # URLs expire after 30 days
	url = URL(id=short_url, original_url=original_url, short_url=short_url, user_id=user_id, expiration_date=expiration_date)
	DB['urls'][short_url] = url
	DB['clicks'][short_url] = 0
	if user_id and user_id in DB['users']:
		DB['users'][user_id].urls.append(url)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB['urls'].get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	if datetime.now() > url.expiration_date:
		return jsonify({'error': 'URL has expired'}), 410
	DB['clicks'][short_url] += 1
	return redirect(url.original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user_id = data.get('user_id')
	if not user_id:
		return jsonify({'error': 'User not found'}), 404
	user = DB['users'].get(user_id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	urls = user.urls
	analytics = []
	for url in urls:
		clicks = DB['clicks'].get(url.id, 0)
		analytics.append({'url': url.short_url, 'clicks': clicks})
	return jsonify({'analytics': analytics}), 200

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user_id = data.get('user_id')
	user = User(id=user_id, urls=[])
	DB['users'][user_id] = user
	return jsonify({'user_id': user_id}), 201

if __name__ == '__main__':
	app.run(debug=True)
