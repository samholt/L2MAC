import hashlib
import requests
from models import URL


class Shortener:
	def __init__(self):
		self.urls = {}

	def shorten_url(self, url, custom_short_link=None):
		if custom_short_link:
			short_url = custom_short_link
		else:
			short_url = hashlib.md5(url.encode()).hexdigest()[:10]
		self.urls[short_url] = URL(original_url=url, short_url=short_url, user='user')
		return short_url

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except requests.exceptions.RequestException:
			return False
