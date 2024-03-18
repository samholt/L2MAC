from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
import datetime
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
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	click_data: list
	expiration_date: datetime.datetime

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
		expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
	url = URL(original_url=original_url, short_url=short_url, user_id=user_id, clicks=0, click_data=[], expiration_date=expiration_date)
	urls[short_url] = url
	users[user_id].urls[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if not url or (url.expiration_date and url.expiration_date < datetime.datetime.now()):
		return jsonify({'error': 'URL not found or expired'}), 404
	url.clicks += 1
	url.click_data.append({'click_time': datetime.datetime.now().isoformat()})
	return redirect(url.original_url, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = urls.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	return jsonify({'clicks': url.clicks, 'click_data': url.click_data}), 200

if __name__ == '__main__':
	app.run(debug=True)
