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
	created_at: datetime.datetime
	expires_at: datetime.datetime
	clicks: int
	user_id: str

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	if not original_url:
		return jsonify({'error': 'URL is required'}), 400
	user_id = data.get('user_id')
	if not user_id:
		return jsonify({'error': 'User ID is required'}), 400
	expires_at = data.get('expires_at')
	if expires_at:
		expires_at = datetime.datetime.strptime(expires_at, '%Y-%m-%dT%H:%M:%S.%f')
	else:
		expires_at = datetime.datetime.max
	short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	url = URL(original_url, short_url, datetime.datetime.now(), expires_at, 0, user_id)
	DB[short_url] = url
	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if url and url.expires_at > datetime.datetime.now():
		url.clicks += 1
		return redirect(url.original, code=302)
	else:
		return jsonify({'error': 'URL not found or expired'}), 404

if __name__ == '__main__':
	app.run(debug=True)
