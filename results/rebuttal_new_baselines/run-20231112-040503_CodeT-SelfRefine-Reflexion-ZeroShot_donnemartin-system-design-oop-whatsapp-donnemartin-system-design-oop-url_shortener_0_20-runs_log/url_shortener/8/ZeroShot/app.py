from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
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
	shortened_url = str(uuid.uuid4())[:8]
	url = URL(original_url, shortened_url, user, 0, datetime.now(), expires_at)
	DB[shortened_url] = url
	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
	url = DB.get(shortened_url)
	if url and url.expires_at > datetime.now():
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
