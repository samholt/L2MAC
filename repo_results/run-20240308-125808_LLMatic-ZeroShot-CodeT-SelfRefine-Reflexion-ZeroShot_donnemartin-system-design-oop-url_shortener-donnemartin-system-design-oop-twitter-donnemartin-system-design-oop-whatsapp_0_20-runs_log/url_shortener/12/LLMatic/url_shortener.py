import hashlib
import requests
from datetime import datetime, timedelta

url_dict = {}


def generate_short_url(url, expiration_minutes=10):
	"""Generate a unique shortened URL.

	Args:
		url (str): The original URL.
		expiration_minutes (int): The number of minutes until the URL expires.

	Returns:
		str: The shortened URL.
	"""
	hash_object = hashlib.md5(url.encode())
	short_url = hash_object.hexdigest()[:10]
	expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
	url_dict[short_url] = {'url': url, 'expiration_time': expiration_time}
	return short_url

def validate_url(url):
	"""Validate a URL.

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

def get_original_url(short_url):
	"""Get the original URL associated with the shortened URL.

	Args:
		short_url (str): The shortened URL.

	Returns:
		str: The original URL, or None if the shortened URL does not exist or has expired.
	"""
	url_data = url_dict.get(short_url)
	if url_data and url_data['expiration_time'] > datetime.now():
		return url_data['url']

