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
	click_data: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	custom_url = data.get('custom')
	expiration = data.get('expiration')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400

	# Validate expiration date
	if expiration:
		try:
			expiration = datetime.fromisoformat(expiration)
		except ValueError:
			return jsonify({'error': 'Invalid expiration date'}), 400

	# Generate shortened URL
	if custom_url:
		if custom_url in DB:
			return jsonify({'error': 'Custom URL already exists'}), 400
		shortened_url = custom_url
	else:
		shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

	# Check if shortened URL already exists
	if shortened_url in DB:
		return jsonify({'error': 'URL already exists'}), 400

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=shortened_url, clicks=0, click_data=[], expiration=expiration)
	DB[shortened_url] = url

	return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<shortened_url>', methods=['GET'])
def redirect_url(shortened_url):
	url = DB.get(shortened_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expiration and datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 400

	# Increment click count and store click data
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.now().isoformat()})

	return redirect(url.original, code=302)

if __name__ == '__main__':
	app.run(debug=True)
