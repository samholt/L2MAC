import hashlib
import requests
from datetime import datetime, timedelta

# Mock database
url_db = {}


def generate_short_url(url, custom_short_url=None, expiration=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_url: Custom short URL provided by the user
	:param expiration: Expiration date/time for the shortened URL
	:return: Shortened URL
	"""
	if custom_short_url:
		short_url = custom_short_url
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]

	# Add URL to database with optional expiration
	url_db[short_url] = {'url': url, 'expiration': expiration}

	return short_url


def validate_url(url):
	"""Validate a given URL.

	:param url: URL to validate
	:return: True if the URL is valid, False otherwise
	"""
	try:
		response = requests.get(url)
		return response.status_code == 200
	except requests.exceptions.RequestException:
		return False


def get_url(short_url):
	"""Retrieve the original URL using the shortened URL.

	:param short_url: Shortened URL
	:return: Original URL if it exists and has not expired, None otherwise
	"""
	url_data = url_db.get(short_url)

	if url_data:
		# Check if URL has expired
		if url_data['expiration'] and datetime.now() > url_data['expiration']:
			# URL has expired, remove from database
			del url_db[short_url]
			return None
		else:
			return url_data['url']

	return None
