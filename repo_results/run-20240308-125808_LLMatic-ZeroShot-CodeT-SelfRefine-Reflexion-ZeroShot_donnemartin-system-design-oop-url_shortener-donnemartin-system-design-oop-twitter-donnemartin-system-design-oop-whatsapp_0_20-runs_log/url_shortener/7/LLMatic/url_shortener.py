import hashlib
import requests
from datetime import datetime, timedelta

# Mock database
mock_db = {}

def generate_short_url(url, custom_short_link=None, expiration_date=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_link: Custom short link
	:param expiration_date: Expiration date/time
	:return: Shortened URL
	"""
	if custom_short_link:
		short_url = custom_short_link
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]

	# Store the short URL, the original URL, and the expiration date in the mock database
	mock_db[short_url] = {'url': url, 'expiration_date': expiration_date}

	return short_url

def validate_url(url):
	"""Validate a URL by making a HTTP request to it.

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
	if short_url in mock_db:
		expiration_date = mock_db[short_url]['expiration_date']
		if expiration_date and datetime.now() > expiration_date:
			return True
	return False
