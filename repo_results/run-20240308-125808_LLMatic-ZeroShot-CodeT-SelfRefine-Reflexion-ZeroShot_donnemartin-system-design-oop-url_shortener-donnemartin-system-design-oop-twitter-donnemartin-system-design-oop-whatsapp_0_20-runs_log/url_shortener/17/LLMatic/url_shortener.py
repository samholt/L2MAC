import hashlib
import requests
from datetime import datetime, timedelta


def generate_short_url(url, custom_short_url=None, expiration_time=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_url: Custom short URL
	:param expiration_time: Expiration time in minutes
	:return: Shortened URL, Expiration datetime
	"""
	if custom_short_url:
		short_url = custom_short_url
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]

	if expiration_time:
		expiration_datetime = datetime.now() + timedelta(minutes=expiration_time)
	else:
		expiration_datetime = None

	return short_url, expiration_datetime


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
