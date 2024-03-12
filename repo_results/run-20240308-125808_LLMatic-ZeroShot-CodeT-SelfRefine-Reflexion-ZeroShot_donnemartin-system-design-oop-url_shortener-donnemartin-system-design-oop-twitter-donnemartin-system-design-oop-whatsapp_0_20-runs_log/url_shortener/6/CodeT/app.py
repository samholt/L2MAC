from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
import datetime
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
	expiration_date: datetime.datetime

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	user_id = data.get('user_id')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(id=short_url, original_url=original_url, short_url=short_url, user_id=user_id, expiration_date=datetime.datetime.now() + datetime.timedelta(days=30))
	DB['urls'][short_url] = url
	if user_id:
		DB['users'][user_id].urls.append(url)
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB['urls'].get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	if datetime.datetime.now() > url.expiration_date:
		return jsonify({'error': 'URL expired'}), 410
	return redirect(url.original_url, code=302)

if __name__ == '__main__':
	app.run(debug=True)
