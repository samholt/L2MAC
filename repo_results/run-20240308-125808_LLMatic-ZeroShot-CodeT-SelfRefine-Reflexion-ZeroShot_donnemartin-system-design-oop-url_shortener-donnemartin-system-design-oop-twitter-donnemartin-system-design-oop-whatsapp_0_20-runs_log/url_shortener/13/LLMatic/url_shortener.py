import hashlib
import requests
from datetime import datetime, timedelta

# Mock database
short_links_db = {}


def generate_short_url(url, custom_short_link=None, expiration_time=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_link: Custom short link
	:param expiration_time: Expiration time for the URL
	:return: Shortened URL
	"""
	if custom_short_link and custom_short_link not in short_links_db:
		short_links_db[custom_short_link] = {'url': url, 'expiration_time': expiration_time}
		return custom_short_link
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]
		short_links_db[short_url] = {'url': url, 'expiration_time': expiration_time}
		return short_url


def validate_url(url):
	"""Validate a URL by making a HTTP request and checking the response status.

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
	if short_url in short_links_db:
		expiration_time = short_links_db[short_url]['expiration_time']
		if expiration_time and datetime.now() > expiration_time:
			return True
	return False
