from flask import Flask, request, redirect, jsonify
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
	custom_alias = data.get('alias')
	expiration = data.get('expiration')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate shortened URL
	shortened_url = custom_alias if custom_alias else ''.join(random.choices(string.ascii_letters + string.digits, k=5))

	# Create URL object and store in DB
	url = URL(original_url, shortened_url, 0, [], expiration)
	DB[shortened_url] = url

	return jsonify({'shortened_url': shortened_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Redirect to original URL
	return redirect(url.original, code=302)

if __name__ == '__main__':
	app.run(debug=True)
