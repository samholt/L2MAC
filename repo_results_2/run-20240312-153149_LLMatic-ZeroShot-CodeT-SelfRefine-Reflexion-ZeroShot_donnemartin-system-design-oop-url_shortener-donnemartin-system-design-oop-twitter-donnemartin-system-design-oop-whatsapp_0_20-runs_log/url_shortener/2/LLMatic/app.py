from flask import Flask, request, redirect, jsonify
import uuid
import requests
import datetime
import re
from collections import defaultdict

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'urls': defaultdict(dict),
	'analytics': defaultdict(dict)
}

# URL validation regex
URL_REGEX = re.compile(
	'^https?://' # http:// or https://
	'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
	'localhost|' # localhost...
	'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
	'(?::\d+)?' # optional port
	'(?:/?|[/?]\S+)$', re.IGNORECASE
)

# Cache for analytics
ANALYTICS_CACHE = {}

@app.route('/shorten', methods=['POST'])
# This function handles the URL shortening request.
# It validates the URL, generates a short URL, and stores it in the database.
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	custom_short_url = data.get('custom_short_url')
	username = data.get('username')
	expiration_date = data.get('expiration_date')

	# Validate the URL
	if not URL_REGEX.match(original_url):
		return 'Invalid URL', 400

	# Handle custom short link
	if custom_short_url:
		if custom_short_url in DATABASE['urls']:
			return 'Custom short link is not available', 400
		else:
			short_url = custom_short_url
	else:
		short_url = str(uuid.uuid4())[:8]

	DATABASE['urls'][short_url] = {'url': original_url, 'username': username, 'expiration_date': expiration_date}
	DATABASE['analytics'][short_url] = {'clicks': 0, 'click_details': []}
	return jsonify({'short_url': short_url}), 200

@app.route('/<short_url>', methods=['GET'])
# This function handles the redirection from the short URL to the original URL.
# It also updates the analytics for the short URL.
def redirect_url(short_url):
	url_data = DATABASE['urls'].get(short_url)
	if url_data:
		if url_data['expiration_date'] and datetime.datetime.now() > datetime.datetime.strptime(url_data['expiration_date'], '%Y-%m-%d %H:%M:%S'):
			return 'URL has expired', 400
		original_url = url_data['url']
		DATABASE['analytics'][short_url]['clicks'] += 1
		DATABASE['analytics'][short_url]['click_details'].append({'timestamp': str(datetime.datetime.now()), 'location': request.remote_addr})
		ANALYTICS_CACHE[short_url] = DATABASE['analytics'][short_url]
		return redirect(original_url)
	else:
		return 'URL not found', 404

@app.route('/analytics/<short_url>', methods=['GET'])
# This function returns the analytics for the given short URL.
def get_analytics(short_url):
	analytics = ANALYTICS_CACHE.get(short_url) or DATABASE['analytics'].get(short_url)
	if analytics:
		return jsonify(analytics), 200
	else:
		return 'URL not found', 404

if __name__ == '__main__':
	app.run(debug=True)
