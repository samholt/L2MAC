import hashlib
import requests
from datetime import datetime


class Shortener:

	def __init__(self):
		self.url_dict = {}

	def shorten_url(self, original_url, custom_short_link=None, expiration_date=None):
		if expiration_date:
			expiration_date = datetime.strptime(expiration_date, '%Y-%m-%dT%H:%M:%S')
		if custom_short_link:
			if custom_short_link in self.url_dict and not self.is_expired(custom_short_link):
				return 'Custom short link already in use'
			else:
				self.url_dict[custom_short_link] = {'url': original_url, 'expiration_date': expiration_date}
				return custom_short_link

		# Create a hash of the original URL
		hash_object = hashlib.md5(original_url.encode())
		shortened_url = hash_object.hexdigest()[:10]

		# Ensure the shortened URL is unique
		while shortened_url in self.url_dict and not self.is_expired(shortened_url):
			shortened_url = hash_object.hexdigest()[:len(shortened_url)+1]

		self.url_dict[shortened_url] = {'url': original_url, 'expiration_date': expiration_date}
		return shortened_url

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except:
			return False

	def is_expired(self, short_url):
		if short_url in self.url_dict:
			expiration_date = self.url_dict[short_url]['expiration_date']
			if expiration_date and datetime.now() > expiration_date:
				return True
		return True
