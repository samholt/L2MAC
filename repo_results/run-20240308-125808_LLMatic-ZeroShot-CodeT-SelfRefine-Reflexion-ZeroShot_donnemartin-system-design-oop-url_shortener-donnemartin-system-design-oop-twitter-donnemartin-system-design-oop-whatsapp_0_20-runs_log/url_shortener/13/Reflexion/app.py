from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import string
import random

app = Flask(__name__)

urls = {}

@dataclass
class URL:
	original: str
	short: str
	created: datetime
	clicks: int
	expiration: datetime

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data['url']
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	urls[short_url] = URL(original_url, short_url, datetime.now(), 0, data.get('expiration'))
	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls.get(short_url)
	if url and (not url.expiration or url.expiration > datetime.now()):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return {'error': 'URL not found or expired'}, 404

if __name__ == '__main__':
	app.run(debug=True)
