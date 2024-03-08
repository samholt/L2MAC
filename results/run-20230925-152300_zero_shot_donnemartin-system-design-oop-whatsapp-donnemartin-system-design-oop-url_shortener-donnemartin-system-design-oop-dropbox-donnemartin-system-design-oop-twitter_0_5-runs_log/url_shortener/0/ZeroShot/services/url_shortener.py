import string
import random
import requests
from datetime import datetime
from geolite2 import geolite2


class URLShortener:
	def __init__(self):
		self.url_data = {}

	def shorten(self, url, custom_alias=None):
		if custom_alias and custom_alias in self.url_data:
			return 'Alias already in use'
		if not self._validate_url(url):
			return 'Invalid URL'
		short_url = custom_alias if custom_alias else self._generate_short_url()
		self.url_data[short_url] = {'url': url, 'clicks': [], 'created_at': datetime.now()}
		return short_url

	def get_url(self, short_url):
		url_data = self.url_data.get(short_url)
		if url_data:
			url_data['clicks'].append(self._get_click_data())
			return url_data['url']
		return None

	def _validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except:
			return False

	def _generate_short_url(self):
		return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

	def _get_click_data(self):
		reader = geolite2.reader()
		location = reader.get(request.remote_addr)
		return {'timestamp': datetime.now(), 'location': location}
