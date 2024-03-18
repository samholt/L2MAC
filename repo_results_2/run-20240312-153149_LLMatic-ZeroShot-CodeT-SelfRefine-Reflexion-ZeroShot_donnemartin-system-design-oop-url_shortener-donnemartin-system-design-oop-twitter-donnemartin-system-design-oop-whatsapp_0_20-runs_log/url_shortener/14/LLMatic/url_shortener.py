import hashlib
import requests
from datetime import datetime, timedelta


def generate_short_url(url):
	"""Generate a unique shortened URL.

	Args:
		url (str): The original URL.

	Returns:
		str: The shortened URL.
	"""
	hash_object = hashlib.md5(url.encode())
	short_url = hash_object.hexdigest()[:10]
	return short_url


def validate_url(url):
	"""Validate a given URL.

	Args:
		url (str): The URL to validate.

	Returns:
		bool: True if the URL is valid, False otherwise.
	"""
	try:
		response = requests.get(url)
		return response.status_code == 200
	except requests.exceptions.RequestException:
		return False


def set_expiration(short_url, hours=24):
	"""Set an expiration date/time for a shortened URL.

	Args:
		short_url (str): The shortened URL.
		hours (int, optional): The number of hours until the URL expires. Defaults to 24.

	Returns:
		datetime: The expiration date/time.
	"""
	expiration = datetime.now() + timedelta(hours=hours)
	return expiration
