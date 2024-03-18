import hashlib
import requests
from datetime import datetime

# Mock database
url_db = {}

def generate_short_url(url, custom_short_link=None, expiration_time=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_link: Custom short link
	:param expiration_time: Expiration date/time
	:return: Shortened URL or custom short link if provided
	"""
	if custom_short_link:
		short_url = custom_short_link
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]

	# If an expiration time is provided, store the short URL and its expiration time in the database
	if expiration_time:
		url_db[short_url] = expiration_time

	return short_url


def validate_url(url):
	"""Validate a given URL.

	:param url: URL to validate
	:return: True if the URL is valid and not expired, False otherwise
	"""
	# If the URL is in the database and it is expired, it is not valid
	if url in url_db:
		if datetime.now() > url_db[url]:
			return False
	else:
		try:
			response = requests.get(url)
			return response.status_code == 200
		except requests.exceptions.RequestException:
			return False

	return True
