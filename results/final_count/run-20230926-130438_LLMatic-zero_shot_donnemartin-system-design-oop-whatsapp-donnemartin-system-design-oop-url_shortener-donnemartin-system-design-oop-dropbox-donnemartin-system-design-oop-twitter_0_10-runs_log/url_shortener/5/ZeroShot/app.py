from flask import Flask, request, jsonify, redirect
from dataclasses import dataclass
from datetime import datetime
import uuid
import requests

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original_url: str
	short_url: str
	user_id: str
	clicks: int
	click_data: list
	expiration_date: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	custom_url = data.get('custom_url')
	user_id = data.get('user_id')
	expiration_date = data.get('expiration_date')

	# Validate URL
	try:
		response = requests.get(original_url)
		if response.status_code != 200:
			return jsonify({'error': 'Invalid URL'}), 400
	except:
		return jsonify({'error': 'Invalid URL'}), 400

	# Generate short URL
	short_url = custom_url if custom_url else str(uuid.uuid4())[:8]

	# Check if short URL already exists
	if short_url in DB:
		return jsonify({'error': 'Short URL already exists'}), 400

	# Create URL object and store in DB
	url = URL(original_url, short_url, user_id, 0, [], expiration_date)
	DB[short_url] = url

	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expiration_date and url.expiration_date < datetime.now():
		return jsonify({'error': 'URL has expired'}), 400

	# Increment click count and store click data
	url.clicks += 1
	url.click_data.append({'click_time': datetime.now().isoformat()})

	return redirect(url.original_url, code=302)

@app.route('/analytics', methods=['GET'])
def get_analytics():
	user_id = request.args.get('user_id')
	if not user_id:
		return jsonify({'error': 'User ID required'}), 400

	# Get all URLs for the user
	user_urls = [url for url in DB.values() if url.user_id == user_id]

	# Prepare analytics data
	analytics_data = []
	for url in user_urls:
		analytics_data.append({
			'original_url': url.original_url,
			'short_url': url.short_url,
			'clicks': url.clicks,
			'click_data': url.click_data
		})

	return jsonify(analytics_data), 200

if __name__ == '__main__':
	app.run(debug=True)
