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
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400
	
	# Check if shortened URL is available
	if shortened_url in DB:
		return jsonify({'error': 'Shortened URL already in use'}), 400
	
	# Create URL object and store in DB
	url = URL(original_url, shortened_url, user, [], expiration)
	DB[shortened_url] = url
	
	return jsonify({'message': 'URL shortened successfully'}), 200

@app.route('/<shortened>', methods=['GET'])
def redirect_url(shortened):
	url = DB.get(shortened)
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	
	# Check if URL has expired
	if datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 400
	
	# Redirect to original URL
	url.clicks.append({'time': datetime.now().isoformat()})
	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user = request.args.get('user')
	urls = [url for url in DB.values() if url.user == user]
	return jsonify({'urls': urls}), 200

if __name__ == '__main__':
	app.run(debug=True)
