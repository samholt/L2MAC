from flask import Flask, request, redirect, jsonify
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

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	shortened_url = data.get('short')
	
	# Validate URL
	try:
		response = requests.get(original_url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return jsonify({'error': 'Invalid URL'}), 400
	
	# Check if short URL is available
	if shortened_url in DB:
		return jsonify({'error': 'Short URL already in use'}), 400
	
	# Create URL object and store in DB
	url = URL(original=original_url, shortened=shortened_url, clicks=0, click_data=[])
	DB[shortened_url] = url
	
	return jsonify({'message': 'URL shortened successfully', 'data': url.__dict__}), 200

@app.route('/<short>', methods=['GET'])
def redirect_url(short):
	url = DB.get(short)
	
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	
	# Update click data
	url.clicks += 1
	url.click_data.append(str(datetime.now()))
	
	return redirect(url.original, code=302)

@app.route('/analytics/<short>', methods=['GET'])
def get_analytics(short):
	url = DB.get(short)
	
	if not url:
		return jsonify({'error': 'URL not found'}), 404
	
	return jsonify({'data': url.__dict__}), 200

if __name__ == '__main__':
	app.run(debug=True)
