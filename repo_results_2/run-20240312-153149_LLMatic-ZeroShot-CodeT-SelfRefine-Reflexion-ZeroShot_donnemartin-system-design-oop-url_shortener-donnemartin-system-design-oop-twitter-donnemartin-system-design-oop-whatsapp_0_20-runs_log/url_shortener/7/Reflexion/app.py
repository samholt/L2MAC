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
	short: str
	clicks: int
	click_data: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	url = request.form.get('url')
	# Validate URL
	try:
		response = requests.get(url)
		response.raise_for_status()
	except (requests.RequestException, ValueError):
		return 'Invalid URL', 400
	# Generate short URL
	short_url = ''.join(choice(ascii_letters + digits) for _ in range(6))
	# Save to DB
	DB[short_url] = URL(original=url, short=short_url, clicks=0, click_data=[])
	return f'Short URL: {short_url}'

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = DB.get(short_url)
	if not url:
		return 'URL not found', 404
	# Increment clicks and save click data
	url.clicks += 1
	url.click_data.append({'time': datetime.now().isoformat(), 'location': request.remote_addr})
	return redirect(url.original)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = DB.get(short_url)
	if not url:
		return 'URL not found', 404
	return jsonify({'clicks': url.clicks, 'click_data': url.click_data})

if __name__ == '__main__':
	app.run(debug=True)
