import hashlib
import requests
from datetime import datetime, timedelta

# Mock database
url_database = {}


def generate_short_url(url, custom_short_link=None, expiration_date=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_link: Custom short link
	:param expiration_date: Expiration date/time
	:return: Shortened URL
	"""
	if custom_short_link and custom_short_link not in url_database:
		url_database[custom_short_link] = {'url': url, 'expiration_date': expiration_date}
		return custom_short_link
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]
		url_database[short_url] = {'url': url, 'expiration_date': expiration_date}
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


def is_url_expired(short_url):
	"""Check if a shortened URL is expired.

	:param short_url: Shortened URL
	:return: True if the URL is expired, False otherwise
	"""
	if short_url in url_database:
		url_data = url_database[short_url]
		if url_data['expiration_date'] and datetime.now() > url_data['expiration_date']:
			return True
	return False
