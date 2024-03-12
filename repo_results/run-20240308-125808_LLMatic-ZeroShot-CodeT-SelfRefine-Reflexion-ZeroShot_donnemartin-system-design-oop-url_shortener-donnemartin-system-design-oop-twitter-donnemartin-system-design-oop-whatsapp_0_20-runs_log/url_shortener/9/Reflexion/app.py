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

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	user = data.get('user')
	expires_at = data.get('expires_at')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[short_url] = URL(original_url, short_url, user, 0, datetime.datetime.now(), expires_at)
	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expires_at or url.expires_at > datetime.datetime.now()):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

if __name__ == '__main__':
	app.run(debug=True)
