import string
import random
from urllib.parse import urlparse
import datetime


class UrlShortener:
	def __init__(self):
		# Initialize URL dictionary
		self.url_dict = {}

	def validate_url(self, url):
		# Validate a URL
		try:
			result = urlparse(url)
			return all([result.scheme, result.netloc])
		except ValueError:
			return False

	def generate_short_url(self):
		# Generate a short URL
		letters_and_digits = string.ascii_letters + string.digits
		short_url = ''.join(random.choice(letters_and_digits) for _ in range(6))
		while short_url in self.url_dict:
			short_url = ''.join(random.choice(letters_and_digits) for _ in range(6))
		return short_url

	def create_short_url(self, original_url, custom_alias=None, expiration_date=None):
		# Create a short URL
		if not self.validate_url(original_url):
			return 'Invalid URL'
		if custom_alias:
			if custom_alias in self.url_dict:
				return 'Custom alias already in use'
			self.url_dict[custom_alias] = {'url': original_url, 'expiration_date': expiration_date}
			return custom_alias
		else:
			short_url = self.generate_short_url()
			self.url_dict[short_url] = {'url': original_url, 'expiration_date': expiration_date}
			return short_url

	def get_original_url(self, short_url):
		# Get the original URL based on the short URL
		url_data = self.url_dict.get(short_url)
		if url_data:
			if url_data['expiration_date'] and datetime.datetime.now() > url_data['expiration_date']:
				self.url_dict.pop(short_url)
				return 'URL expired'
			return url_data['url']
		return 'URL not found'

	def get_all_urls(self):
		# Get all URLs
		return self.url_dict

	def delete_url(self, short_url):
		# Delete a URL
		if short_url in self.url_dict:
			self.url_dict.pop(short_url)
			return 'URL deleted successfully'
		return 'URL not found'

