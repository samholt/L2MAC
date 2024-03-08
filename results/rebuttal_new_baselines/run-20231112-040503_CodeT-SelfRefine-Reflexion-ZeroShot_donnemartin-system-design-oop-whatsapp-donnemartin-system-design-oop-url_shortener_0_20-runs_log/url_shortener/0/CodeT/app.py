from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
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
	user_id: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user_id = data.get('user_id')
	expires_at = data.get('expires_at')
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url, short_url, 0, datetime.now(), expires_at, user_id)
	DB[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if url and url.expires_at > datetime.now():
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user_id = request.args.get('user_id')
	urls = [url for url in DB.values() if url.user_id == user_id]
	return jsonify({'urls': urls}), 200

if __name__ == '__main__':
	app.run(debug=True)
