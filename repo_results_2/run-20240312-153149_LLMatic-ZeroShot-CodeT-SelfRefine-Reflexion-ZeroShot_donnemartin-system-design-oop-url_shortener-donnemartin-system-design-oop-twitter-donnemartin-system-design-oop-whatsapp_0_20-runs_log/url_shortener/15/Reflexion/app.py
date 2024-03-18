from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import requests
from geolite2 import geolite2

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class URL:
	original: str
	shortened: str
	clicks: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	shortened_url = data.get('shortened')

	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400

	# Check if shortened URL is available
	if shortened_url in DATABASE:
		return jsonify({'error': 'Shortened URL is already in use'}), 400

	# Create new URL object and store in database
	DATABASE[shortened_url] = URL(original_url, shortened_url, [])

	return jsonify({'shortened_url': shortened_url}), 201

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
	url = DATABASE.get(shortened_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Record click
	url.clicks.append(datetime.now().isoformat())

	return redirect(url.original, code=302)

@app.route('/analytics/<shortened_url>', methods=['GET'])
def get_analytics(shortened_url):
	url = DATABASE.get(shortened_url)

	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Get click data
	click_data = url.clicks

	return jsonify({'clicks': click_data}), 200

if __name__ == '__main__':
	app.run(debug=True)
