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
	click_data: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	shortened_url = data.get('shortened')
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
	url = URL(original=original_url, shortened=shortened_url, clicks=0, click_data=[], expiration=datetime.strptime(expiration, '%Y-%m-%d %H:%M:%S'))
	DB[shortened_url] = url

	return jsonify({'message': 'URL shortened successfully', 'data': url.__dict__}), 200

@app.route('/<shortened>', methods=['GET'])
def redirect_url(shortened):
	url = DB.get(shortened)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if datetime.now() > url.expiration:
		return jsonify({'error': 'URL has expired'}), 400

	# Increment click count and store click data
	url.clicks += 1
	url.click_data.append({'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

	return redirect(url.original, code=302)

@app.route('/analytics/<shortened>', methods=['GET'])
def get_analytics(shortened):
	url = DB.get(shortened)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	return jsonify({'data': url.__dict__}), 200

if __name__ == '__main__':
	app.run(debug=True)
