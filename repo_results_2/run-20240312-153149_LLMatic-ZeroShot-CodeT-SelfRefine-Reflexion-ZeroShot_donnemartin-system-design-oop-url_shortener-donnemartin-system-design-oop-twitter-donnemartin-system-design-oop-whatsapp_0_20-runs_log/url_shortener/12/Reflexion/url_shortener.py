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
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	creation_date = datetime.datetime.now()
	expiration_date = creation_date + datetime.timedelta(days=30)
	clicks = 0
	user_id = data.get('user_id', '')
	url = URL(original_url, short_url, creation_date, expiration_date, clicks, user_id)
	urls_db[short_url] = url
	if user_id:
		if user_id in users_db:
			users_db[user_id].urls.append(url)
		else:
			users_db[user_id] = User(user_id, [url])
	return jsonify({'short_url': short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls_db.get(short_url)
	if url and url.expiration_date > datetime.datetime.now():
		url.clicks += 1
		return redirect(url.original_url, code=302)
	else:
		return 'URL expired or does not exist', 404

@app.route('/user/<user_id>', methods=['GET'])
def get_user_urls(user_id):
	user = users_db.get(user_id)
	if user:
		return jsonify([url.__dict__ for url in user.urls])
	else:
		return 'User does not exist', 404

if __name__ == '__main__':
	app.run(debug=True)
