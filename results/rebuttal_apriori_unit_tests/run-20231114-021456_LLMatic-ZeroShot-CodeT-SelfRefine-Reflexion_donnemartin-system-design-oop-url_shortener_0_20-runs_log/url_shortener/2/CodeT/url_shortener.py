import string
import random
from datetime import datetime
from flask import Flask, request, redirect

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'urls': {}
}

# Helper Functions

def generate_short_url():
	return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def validate_url(url):
	# Placeholder validation
	return url.startswith('http')

def check_expiration(url):
	return DATABASE['urls'][url]['expiration'] < datetime.now()

# Routes

@app.route('/shorten', methods=['POST'])

def shorten_url():
	data = request.get_json()
	url = data.get('url')
	custom_slug = data.get('custom_slug')
	expiration_time = data.get('expiration_time')

	if not validate_url(url):
		return {'error': 'Invalid URL'}, 400

	short_url = custom_slug if custom_slug else generate_short_url()
	DATABASE['urls'][short_url] = {
		'url': url,
		'clicks': 0,
		'click_dates': [],
		'click_geolocations': [],
		'expiration': expiration_time
	}

	return {'short_url': short_url}, 200

@app.route('/<short_url>', methods=['GET'])

def redirect_to_url(short_url):
	if short_url not in DATABASE['urls'] or check_expiration(short_url):
		return {'error': 'URL not found or expired'}, 404

	DATABASE['urls'][short_url]['clicks'] += 1
	DATABASE['urls'][short_url]['click_dates'].append(datetime.now())
	# Placeholder geolocation
	DATABASE['urls'][short_url]['click_geolocations'].append('Unknown')

	return redirect(DATABASE['urls'][short_url]['url'])

if __name__ == '__main__':
	app.run(debug=True)
