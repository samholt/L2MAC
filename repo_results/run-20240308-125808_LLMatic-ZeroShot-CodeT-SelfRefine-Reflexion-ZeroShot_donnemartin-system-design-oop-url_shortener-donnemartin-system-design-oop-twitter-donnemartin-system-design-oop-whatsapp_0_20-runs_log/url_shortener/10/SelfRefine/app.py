from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests
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
	short_url = data.get('short_url')
	expires_at = data.get('expires_at')
	user_id = data.get('user_id', 'anonymous')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except requests.exceptions.RequestException:
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL
	if not short_url:
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

	# Check if short URL is already in use
	if short_url in DB:
		return jsonify({'error': 'Short URL already in use'}), 400

	# Parse expires_at to datetime
	if expires_at:
		expires_at = datetime.fromisoformat(expires_at)

	# Create URL object and store in DB
	url = URL(original_url, short_url, 0, datetime.now(), expires_at, user_id)
	DB[short_url] = url

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expires_at and url.expires_at < datetime.now():
		return jsonify({'error': 'URL has expired'}), 400

	# Increment click count
	url.clicks += 1

	return redirect(url.original, code=302)

if __name__ == '__main__':
	app.run(debug=True)
