import hashlib
import requests

# Mock database
url_db = {}

def generate_short_url(url, custom_short_url=None):
	"""Generate a unique shortened URL.

	:param url: Original URL
	:param custom_short_url: Custom short URL
	:return: Shortened URL
	"""
	if custom_short_url and custom_short_url not in url_db:
		url_db[custom_short_url] = url
		return custom_short_url
	else:
		hash_object = hashlib.md5(url.encode())
		short_url = hash_object.hexdigest()[:10]
		while short_url in url_db:
			hash_object = hashlib.md5((url + short_url).encode())
			short_url = hash_object.hexdigest()[:10]
		url_db[short_url] = url
		return short_url

def validate_url(url):
	"""Validate a given URL is active and legitimate.

	:param url: URL to validate
	:return: Boolean indicating if the URL is valid
	"""
	try:
		response = requests.get(url)
		return response.status_code == 200
	except requests.exceptions.RequestException:
		return False
