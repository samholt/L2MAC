from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass, asdict
import datetime
import random
import string
import hashlib

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	short: str
	clicks: int
	created_at: datetime.datetime
	expires_at: datetime.datetime
	user_id: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user_id = data.get('user_id')
	short_url = hashlib.md5(original_url.encode()).hexdigest()[:5]
	counter = 0
	while short_url in DB:
		counter += 1
		short_url = hashlib.md5((original_url + str(counter)).encode()).hexdigest()[:5]
	url = URL(original=original_url, short=short_url, clicks=0, created_at=datetime.datetime.now(), expires_at=None, user_id=user_id)
	DB[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB.get(short_url)
	if url and (not url.expires_at or url.expires_at > datetime.datetime.now()):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return 'URL not found or expired', 404

@app.route('/details/<short_url>', methods=['GET'])
def get_url_details(short_url):
	url = DB.get(short_url)
	if url:
		return jsonify(asdict(url))
	else:
		return 'URL not found', 404

if __name__ == '__main__':
	app.run(debug=True)
