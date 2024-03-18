from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import string
import random

app = Flask(__name__)

# Mock database
urls = {}
users = {}

@dataclass
class URL:
	original: str
	short: str
	user: str
	clicks: int
	created_at: datetime
	expires_at: datetime
	location: str

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('original_url')
	user = data.get('user')
	expires_at = data.get('expires_at')
	custom_short = data.get('custom_short')

	# Check if custom short link is provided and available
	if custom_short and custom_short not in urls:
		short_url = custom_short
	else:
		# Generate a random short URL
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

	# Create a new URL object and store it in the database
	urls[short_url] = URL(original_url, short_url, user, 0, datetime.now(), expires_at, '')

	return {'short_url': short_url}

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	url = urls.get(short_url)

	if url and (not url.expires_at or url.expires_at > datetime.now()):
		# Update click count and location
		url.clicks += 1
		url.location = 'Mock Location'

		return redirect(url.original)

	return {'error': 'URL not found or expired'}, 404

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = urls.get(short_url)

	if url:
		return {'original_url': url.original, 'short_url': url.short, 'clicks': url.clicks, 'created_at': url.created_at, 'expires_at': url.expires_at, 'location': url.location}

	return {'error': 'URL not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
