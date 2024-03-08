from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests

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

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	shortened_url = data.get('shortened')
	expires_at = data.get('expires_at')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if shortened URL is available
	if shortened_url in DB:
		return jsonify({'error': 'Shortened URL is already in use'}), 400

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=shortened_url, clicks=0, created_at=datetime.now(), expires_at=expires_at)
	DB[shortened_url] = url

	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_url(shortened_url):
	url = DB.get(shortened_url)

	# Check if URL exists and has not expired
	if not url or datetime.now() > url.expires_at:
		return jsonify({'error': 'URL not found or expired'}), 404

	# Increment click count and redirect
	url.clicks += 1
	return redirect(url.original, code=302)

if __name__ == '__main__':
	app.run(debug=True)
