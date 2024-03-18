import hashlib
import requests
import datetime


class URLShortener:
	def __init__(self):
		self.url_map = {}

	def generate_short_url(self, url, custom_short_link=None, expiration_date=None):
		"""Generate a unique shortened URL.

		:param url: Original URL
		:param custom_short_link: Custom short link provided by the user
		:param expiration_date: Expiration date/time of the URL
		:return: Shortened URL
		"""
		if custom_short_link:
			short_url = custom_short_link
		else:
			hash_object = hashlib.md5(url.encode())
			short_url = hash_object.hexdigest()[:10]
		self.url_map[short_url] = {'url': url, 'expiration_date': expiration_date}
		return short_url

	def get_original_url(self, short_url):
		"""Get the original URL for a given short URL.

		:param short_url: Short URL
		:return: Original URL if found and not expired, None otherwise
		"""
		url_data = self.url_map.get(short_url)
		if url_data and (not url_data['expiration_date'] or datetime.datetime.now() < url_data['expiration_date']):
			return url_data['url']

	def get_all_urls(self):
		"""Get all shortened URLs.

		:return: Dictionary of all shortened URLs
		"""
		return self.url_map

	def delete_url(self, short_url):
		"""Delete a shortened URL.

		:param short_url: Short URL to delete
		:return: None
		"""
		if short_url in self.url_map:
			del self.url_map[short_url]

	def validate_url(self, url):
		"""Validate a URL by sending a GET request and checking the response status.

		:param url: URL to validate
		:return: True if the URL is valid, False otherwise
		"""
		try:
			response = requests.get(url)
			return response.status_code == 200
		except requests.exceptions.RequestException:
			return False
