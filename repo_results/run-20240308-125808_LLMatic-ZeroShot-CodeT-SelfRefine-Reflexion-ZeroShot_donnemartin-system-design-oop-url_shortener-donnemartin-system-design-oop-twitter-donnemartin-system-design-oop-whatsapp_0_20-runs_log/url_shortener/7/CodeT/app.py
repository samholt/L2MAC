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
	user: str
	clicks: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	short_url = data.get('short_url')
	user = data.get('user')
	expiration = data.get('expiration')
	
	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400
	
	# Check if short URL is available
	if short_url in DB:
		return jsonify({'error': 'Short URL already in use'}), 400
	
	# Create URL object and store in DB
	url = URL(original=original_url, shortened=short_url, user=user, clicks=[], expiration=datetime.fromisoformat(expiration))
	DB[short_url] = url
	
	return jsonify({'message': 'URL shortened successfully', 'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	
	if not url or url.expiration < datetime.now():
		return jsonify({'error': 'URL not found or expired'}), 404
	
	# Record click
	url.clicks.append({'timestamp': datetime.now().isoformat()})
	
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user = request.args.get('user')
	
	# Get all URLs for user
	urls = [url for url in DB.values() if url.user == user]
	
	# Prepare analytics data
	data = [{'original': url.original, 'shortened': url.shortened, 'clicks': url.clicks} for url in urls]
	
	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True)
