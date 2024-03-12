from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
import datetime
import random
import string

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
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url, short_url, 0, datetime.datetime.now(), None, user_id)
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

if __name__ == '__main__':
	app.run(debug=True)
