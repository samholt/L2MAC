import hashlib
import requests
from datetime import datetime, timedelta


def generate_short_url(url):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:return: Shortened URL
	"""
	hash_object = hashlib.md5(url.encode())
	short_url = hash_object.hexdigest()[:10]
	return short_url


def validate_url(url):
	"""Validate a URL by sending a GET request and checking the response status.

	:param url: URL to validate
	:return: True if the URL is valid, False otherwise
	"""
	try:
		response = requests.get(url)
		return response.status_code == 200
	except requests.exceptions.RequestException:
		return False


def store_url(app, short_url, original_url, expiration_minutes):
	"""Store the original URL and its shortened version in the mock database.

	:param app: Flask application
	:param short_url: Shortened URL
	:param original_url: Original URL
	:param expiration_minutes: The number of minutes after which the URL should expire
	"""
	expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
	app.url_db[short_url] = {'url': original_url, 'expiration_time': expiration_time}


def get_url(app, short_url):
	"""Retrieve the original URL using the shortened URL.

	:param app: Flask application
	:param short_url: Shortened URL
	:return: Original URL if it exists and has not expired, None otherwise
	"""
	url_data = app.url_db.get(short_url)
	if url_data and datetime.now() <= url_data['expiration_time']:
		return url_data['url']
	return None
