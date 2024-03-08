import string
import random
from urllib.parse import urlparse
from datetime import datetime, timedelta


class URLShortener:
	def __init__(self):
		self.url_dict = {}

	def validate_url(self, url):
		parsed_url = urlparse(url)
		return all([parsed_url.scheme, parsed_url.netloc])

	def generate_short_url(self, url, expiration_minutes=0):
		if url in self.url_dict:
			return self.url_dict[url]['short_url']
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			expiration_time = datetime.now() + timedelta(minutes=expiration_minutes) if expiration_minutes else None
			self.url_dict[url] = {'short_url': short_url, 'expiration_time': expiration_time}
			return short_url

	def custom_short_url(self, url, custom, expiration_minutes=0):
		if custom in [value['short_url'] for value in self.url_dict.values()]:
			return 'Custom URL already exists'
		else:
			expiration_time = datetime.now() + timedelta(minutes=expiration_minutes) if expiration_minutes else None
			self.url_dict[url] = {'short_url': custom, 'expiration_time': expiration_time}
			return custom

	def get_original_url(self, short_url):
		for url, value in self.url_dict.items():
			if value['short_url'] == short_url:
				if value['expiration_time'] and datetime.now() > value['expiration_time']:
					return 'URL expired'
				else:
					return url
		return 'URL not found'
