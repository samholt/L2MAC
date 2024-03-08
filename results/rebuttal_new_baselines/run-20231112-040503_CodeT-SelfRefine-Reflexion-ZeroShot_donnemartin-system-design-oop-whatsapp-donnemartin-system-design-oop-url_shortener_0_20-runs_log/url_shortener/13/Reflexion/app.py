from flask import Flask, request, jsonify
from dataclasses import dataclass
import datetime

app = Flask(__name__)

# Mock database
users = {}
urls = {}

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
	clicks: int
	clicks_data: list
	expiration_date: datetime.datetime

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user_id = data['user_id']
	if user_id in users:
		return jsonify({'message': 'User already exists.'}), 400
	users[user_id] = User(user_id, [])
	return jsonify({'message': 'User created successfully.'}), 201

@app.route('/create_url', methods=['POST'])
def create_url():
	data = request.get_json()
	url_id = data['url_id']
	original_url = data['original_url']
	short_url = data['short_url']
	user_id = data['user_id']
	expiration_date = datetime.datetime.strptime(data['expiration_date'], '%Y-%m-%d %H:%M:%S')
	if url_id in urls:
		return jsonify({'message': 'URL already exists.'}), 400
	if user_id not in users:
		return jsonify({'message': 'User not found.'}), 404
	urls[url_id] = URL(url_id, original_url, short_url, user_id, 0, [], expiration_date)
	users[user_id].urls.append(url_id)
	return jsonify({'message': 'URL created successfully.'}), 201

@app.route('/get_url/<url_id>', methods=['GET'])
def get_url(url_id):
	if url_id not in urls:
		return jsonify({'message': 'URL not found.'}), 404
	url = urls[url_id]
	if datetime.datetime.now() > url.expiration_date:
		return jsonify({'message': 'URL expired.'}), 410
	url.clicks += 1
	url.clicks_data.append({'click_time': datetime.datetime.now().isoformat()})
	return jsonify({'original_url': url.original_url}), 302

@app.route('/get_user_urls/<user_id>', methods=['GET'])
def get_user_urls(user_id):
	if user_id not in users:
		return jsonify({'message': 'User not found.'}), 404
	user_urls = [urls[url_id] for url_id in users[user_id].urls]
	return jsonify({'urls': [url.__dict__ for url in user_urls]}), 200

if __name__ == '__main__':
	app.run(debug=True)
