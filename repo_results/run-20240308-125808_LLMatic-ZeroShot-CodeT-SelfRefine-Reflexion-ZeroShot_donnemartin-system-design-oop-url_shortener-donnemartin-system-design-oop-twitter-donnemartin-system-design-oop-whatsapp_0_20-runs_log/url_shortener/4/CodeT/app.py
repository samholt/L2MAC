from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import pytz
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
	created_at: datetime
	expires_at: datetime
	owner: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	DB[short_url] = URL(original_url, short_url, 0, datetime.now(pytz.utc), None, data.get('user'))
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if url and (not url.expires_at or url.expires_at > datetime.now(pytz.utc)):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return 'URL not found or expired', 404

if __name__ == '__main__':
	app.run(debug=True)
