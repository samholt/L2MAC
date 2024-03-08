from flask import Flask, request, jsonify, redirect
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
	clicks: int
	click_data: list
	expiration_date: datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = str(uuid.uuid4())
	users[user_id] = User(id=user_id, urls={})
	return jsonify({'user_id': user_id}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	url_id = str(uuid.uuid4())
	short_url = data.get('short_url', url_id[:8])
	urls[url_id] = URL(
		id=url_id,
		original_url=data['original_url'],
		short_url=short_url,
		user_id=data['user_id'],
		clicks=0,
		click_data=[],
		expiration_date=data.get('expiration_date', None)
	)
	users[data['user_id']].urls[url_id] = urls[url_id]
	return jsonify({'url_id': url_id, 'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	for url in urls.values():
		if url.short_url == short_url:
			url.clicks += 1
			url.click_data.append(datetime.now())
			return redirect(url.original_url, code=302)
	return 'URL not found', 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	url = urls.get(data['url_id'])
	if url:
		return jsonify({'clicks': url.clicks, 'click_data': url.click_data}), 200
	return 'URL not found', 404

if __name__ == '__main__':
	app.run(debug=True)
