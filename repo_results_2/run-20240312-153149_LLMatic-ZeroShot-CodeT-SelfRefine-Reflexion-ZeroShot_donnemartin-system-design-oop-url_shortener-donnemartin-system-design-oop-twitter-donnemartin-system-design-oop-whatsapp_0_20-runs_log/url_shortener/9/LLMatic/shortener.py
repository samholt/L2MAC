import string
import random
import requests
import datetime


class Shortener:
	def __init__(self):
		self.url_mapping = {}

	def shorten_url(self, original_url, expiration=None):
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
		while short_url in self.url_mapping:
			short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
		self.url_mapping[short_url] = {'url': original_url, 'expiration': expiration}
		return short_url

	def get_original_url(self, short_url):
		url_data = self.url_mapping.get(short_url)
		if url_data and (url_data['expiration'] is None or url_data['expiration'] > datetime.datetime.now()):
			return url_data['url']
		return None

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except requests.exceptions.RequestException:
			return False

