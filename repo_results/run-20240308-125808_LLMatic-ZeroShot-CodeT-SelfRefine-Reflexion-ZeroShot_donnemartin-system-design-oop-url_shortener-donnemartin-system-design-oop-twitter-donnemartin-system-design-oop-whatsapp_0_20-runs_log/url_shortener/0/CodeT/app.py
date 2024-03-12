from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import requests

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: int
	click_data: list
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
	if shortened_url in urls:
		return jsonify({'error': 'Shortened URL already in use'}), 400

	# Create URL object and store in database
	url = URL(original=original_url, shortened=shortened_url, user=user, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S'))
	urls[shortened_url] = url

	return jsonify({'message': 'URL shortened successfully', 'data': url.__dict__}), 200

@app.route('/<shortened>', methods=['GET'])
def redirect_url(shortened):
	url = urls.get(shortened)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 400

	# Increment click count and store click data
	url.clicks += 1
	url.click_data.append({'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'location': request.remote_addr})

	return redirect(url.original, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	data = request.get_json()
	user = data.get('user')

	# Get all URLs for the user
	user_urls = [url.__dict__ for url in urls.values() if url.user == user]

	return jsonify({'data': user_urls}), 200

@app.route('/admin', methods=['GET'])
def get_admin():
	# Get all URLs
	all_urls = [url.__dict__ for url in urls.values()]

	return jsonify({'data': all_urls}), 200

if __name__ == '__main__':
	app.run(debug=True)
