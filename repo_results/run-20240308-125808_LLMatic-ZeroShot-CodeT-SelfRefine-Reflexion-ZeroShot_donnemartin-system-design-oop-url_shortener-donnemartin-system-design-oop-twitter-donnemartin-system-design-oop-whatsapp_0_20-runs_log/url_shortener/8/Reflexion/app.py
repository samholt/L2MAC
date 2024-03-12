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
	short_url = data.get('short')
	expires_at = data.get('expires_at')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if short URL is available
	if short_url in DB:
		return jsonify({'error': 'Short URL already in use'}), 400

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=short_url, clicks=0, created_at=datetime.now(), expires_at=expires_at)
	DB[short_url] = url

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if datetime.now() > url.expires_at:
		return jsonify({'error': 'URL has expired'}), 400

	# Increment click count and redirect
	url.clicks += 1
	return redirect(url.original, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Return analytics data
	data = {
		'original_url': url.original,
		'short_url': url.shortened,
		'clicks': url.clicks,
		'created_at': url.created_at,
		'expires_at': url.expires_at
	}
	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True)
