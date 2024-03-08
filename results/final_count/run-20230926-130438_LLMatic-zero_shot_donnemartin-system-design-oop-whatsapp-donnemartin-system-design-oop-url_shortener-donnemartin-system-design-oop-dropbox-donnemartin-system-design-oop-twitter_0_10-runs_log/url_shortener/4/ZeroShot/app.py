from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import pytz
import uuid

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	created_at: datetime
	expires_at: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	expires_at = data.get('expires_at')
	short_url = str(uuid.uuid4())[:8]
	url = URL(original=original_url, shortened=short_url, user=user, clicks=0, created_at=datetime.now(pytz.utc), expires_at=expires_at)
	DB[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if url and url.expires_at > datetime.now(pytz.utc):
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
