from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
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

@app.route('/create_user', methods=['POST'])
def create_user():
	user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	user = User(id=user_id, urls=[])
	DB['users'][user_id] = user
	return jsonify(user_id=user_id), 201

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	original_url = request.json.get('original_url')
	user_id = request.json.get('user_id')
	expiration_date = request.json.get('expiration_date')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(id=short_url, original_url=original_url, short_url=short_url, user_id=user_id, expiration_date=expiration_date)
	DB['urls'][short_url] = url
	DB['users'][user_id].urls.append(url)
	return jsonify(short_url=short_url), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB['urls'].get(short_url)
	if url and datetime.now() <= url.expiration_date:
		DB['clicks'][short_url] = DB['clicks'].get(short_url, 0) + 1
		return redirect(url.original_url, code=302)
	else:
		return 'URL not found or expired', 404

@app.route('/analytics', methods=['GET'])
def analytics():
	user_id = request.args.get('user_id')
	user = DB['users'].get(user_id)
	if user:
		urls = user.urls
		clicks = {url.id: DB['clicks'].get(url.id, 0) for url in urls}
		return jsonify(clicks=clicks), 200
	else:
		return 'User not found', 404

if __name__ == '__main__':
	app.run(debug=True)
