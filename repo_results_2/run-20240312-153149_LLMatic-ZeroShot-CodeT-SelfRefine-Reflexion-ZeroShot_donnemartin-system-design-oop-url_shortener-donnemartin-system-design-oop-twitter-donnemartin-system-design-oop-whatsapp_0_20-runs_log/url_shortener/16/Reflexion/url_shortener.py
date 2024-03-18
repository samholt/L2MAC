from flask import Flask, request, redirect
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
	user: str
	clicks: int
	expiration_date: datetime.datetime

@dataclass
class User:
	username: str
	urls: list

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['original_url']
	user = data.get('user')
	expiration_date = data.get('expiration_date')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url, short_url, user, 0, expiration_date)
	urls_db[short_url] = url
	if user:
		if user in users_db:
			users_db[user].urls.append(url)
		else:
			new_user = User(user, [url])
			users_db[user] = new_user
	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls_db.get(short_url)
	if url and (not url.expiration_date or url.expiration_date > datetime.datetime.now()):
		url.clicks += 1
		return redirect(url.original_url, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

if __name__ == '__main__':
	app.run(debug=True)
