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
	shortened: str
	clicks: int
	created_at: datetime.datetime
	expires_at: datetime.datetime
	owner: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = data.get('short_url', ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)))
	expires_at = data.get('expires_at')
	if expires_at:
		expires_at = datetime.datetime.strptime(expires_at, '%Y-%m-%d')
	DB[short_url] = URL(original_url, short_url, 0, datetime.datetime.now(), expires_at, data.get('user'))
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if url and (not url.expires_at or url.expires_at > datetime.datetime.now()):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
