from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
users = {}
urls = {}

@dataclass
class User:
	id: str
	urls: dict

@dataclass
class URL:
	id: str
	original_url: str
	short_url: str
	user_id: str
	clicks: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = str(uuid.uuid4())
	users[user_id] = User(id=user_id, urls={})
	return jsonify({'user_id': user_id}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	user_id = data.get('user_id')
	original_url = data.get('original_url')
	short_url = data.get('short_url', str(uuid.uuid4())[:8])
	expiration_date = data.get('expiration_date')
	if expiration_date:
		expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	url_id = str(uuid.uuid4())
	urls[url_id] = URL(id=url_id, original_url=original_url, short_url=short_url, user_id=user_id, clicks=[], expiration_date=expiration_date)
	users[user_id].urls[url_id] = urls[url_id]
	return jsonify({'url_id': url_id, 'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	for url in urls.values():
		if url.short_url == short_url:
			if url.expiration_date and url.expiration_date < datetime.now():
				return 'URL expired', 410
			url.clicks.append({'click_time': datetime.now().isoformat()})
			return redirect(url.original_url, code=302)
	return 'URL not found', 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user_id = data.get('user_id')
	user = users.get(user_id)
	if not user:
		return 'User not found', 404
	analytics = {}
	for url in user.urls.values():
		analytics[url.id] = {'original_url': url.original_url, 'short_url': url.short_url, 'clicks': url.clicks}
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
