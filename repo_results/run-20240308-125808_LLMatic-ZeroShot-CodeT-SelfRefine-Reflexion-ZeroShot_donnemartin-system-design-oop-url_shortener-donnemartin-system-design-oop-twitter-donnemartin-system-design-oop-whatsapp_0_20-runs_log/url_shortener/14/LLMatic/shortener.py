import string
import random
import requests
from datetime import datetime


class Shortener:
	def __init__(self):
		self.url_dict = {}
		self.expiration_dict = {}

	def shorten_url(self, original_url):
		short_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
		while short_url in self.url_dict:
			short_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
		self.url_dict[short_url] = original_url
		return 'http://short.url/' + short_url

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except:
			return False

	def set_expiration(self, short_url, expiration_datetime):
		short_url = short_url.replace('http://short.url/', '')
		if short_url in self.url_dict:
			self.expiration_dict[short_url] = expiration_datetime
			return True
		return False

	def get_url(self, short_url):
		short_url = short_url.replace('http://short.url/', '')
		if short_url in self.url_dict and (short_url not in self.expiration_dict or datetime.now() < self.expiration_dict[short_url]):
			return self.url_dict[short_url]
		return None
