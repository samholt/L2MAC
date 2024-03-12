from flask import Flask, request, redirect
from dataclasses import dataclass
import datetime
import random
import string

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	short: str
	user: str
	clicks: int
	created_at: datetime.datetime
	expires_at: datetime.datetime

@dataclass
class User:
	username: str
	password: str
	urls: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	user = data.get('user')
	expires_at = data.get('expires_at')
	url = URL(original=original_url, short=short_url, user=user, clicks=0, created_at=datetime.datetime.now(), expires_at=expires_at)
	urls[short_url] = url
	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expires_at or url.expires_at > datetime.datetime.now()):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')
	if user:
		user_urls = [url for url in urls.values() if url.user == user]
		return {'urls': user_urls}, 200
	else:
		return {'urls': urls.values()}, 200

if __name__ == '__main__':
	app.run(debug=True)
