import hashlib
import requests
from datetime import datetime

# Mock database
url_database = {}

def generate_short_url(url, custom_short_url=None, expiration_date=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_url: Custom short URL
	:param expiration_date: Expiration date/time for the shortened URL
	:return: Shortened URL
	"""
	if custom_short_url and custom_short_url not in url_database.keys():
		short_url = custom_short_url
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


def is_expired(short_url):
	"""Check if a shortened URL is expired.

	:param short_url: Shortened URL
	:return: True if the URL is expired, False otherwise
	"""
	if short_url in url_database.keys():
		expiration_date = url_database[short_url]['expiration_date']
		if expiration_date and datetime.now() > datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S'):
			return True
	return False
