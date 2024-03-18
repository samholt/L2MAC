import string
import random
from urllib.parse import urlparse
from datetime import datetime
import requests

class Shortener:
	def __init__(self):
		self.url_map = {}
		self.analytics = {}
		self.users = {}
		self.total_users = 0
		self.expiration = {}

	def validate_url(self, url):
		parsed = urlparse(url)
		return all([parsed.scheme, parsed.netloc])

	def generate_short_url(self, url, expiration=None):
		if url in self.url_map:
			return self.url_map[url]
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			self.url_map[url] = short_url
			self.analytics[short_url] = {'clicks': 0, 'timestamps': [], 'locations': []}
			self.expiration[short_url] = expiration
			return short_url

	def custom_short_url(self, url, custom, expiration=None):
		if custom in self.url_map.values():
			return 'Custom URL already exists'
		elif url in self.url_map:
			return 'URL already has a short URL'
		else:
			self.url_map[url] = custom
			self.analytics[custom] = {'clicks': 0, 'timestamps': [], 'locations': []}
			self.expiration[custom] = expiration
			return custom

	def get_original_url(self, short_url, ip_address):
		for url, s_url in self.url_map.items():
			if s_url == short_url:
				if self.expiration[short_url] and datetime.now() > self.expiration[short_url]:
					return 'URL has expired'
				self.analytics[short_url]['clicks'] += 1
				self.analytics[short_url]['timestamps'].append(datetime.now())
				response = requests.get(f'http://ip-api.com/json/{ip_address}')
				self.analytics[short_url]['locations'].append(response.json()['country'])
				return url
		return None

	def get_analytics(self, short_url):
		return self.analytics.get(short_url, 'Short URL not found')
