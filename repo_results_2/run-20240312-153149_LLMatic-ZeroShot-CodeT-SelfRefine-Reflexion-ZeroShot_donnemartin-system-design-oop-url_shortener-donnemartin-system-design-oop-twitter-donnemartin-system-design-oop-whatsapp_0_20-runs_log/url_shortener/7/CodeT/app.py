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
	shortened_url = data.get('shortened')
	user = data.get('user')
	expiration = data.get('expiration')
	
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
	url = URL(original_url, shortened_url, user, [], expiration)
	DB[shortened_url] = url
	
	return jsonify({'message': 'URL shortened successfully', 'data': url}), 200

@app.route('/<shortened>', methods=['GET'])
def redirect_to_url(shortened):
	url = DB.get(shortened)
	
	# Check if URL exists and has not expired
	if not url or datetime.now() > url.expiration:
		return jsonify({'error': 'URL not found or expired'}), 404
	
	# Record click
	url.clicks.append({'timestamp': datetime.now(), 'location': request.remote_addr})
	
	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user = request.args.get('user')
	
	# Get all URLs for user
	urls = [url for url in DB.values() if url.user == user]
	
	return jsonify({'data': urls}), 200

if __name__ == '__main__':
	app.run(debug=True)
