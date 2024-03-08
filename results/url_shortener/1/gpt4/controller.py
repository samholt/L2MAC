from model import URL
from datetime import datetime, timedelta
import random
import string


class URLController:
	def __init__(self):
		self.urls = {}

	def create_url(self, original_url, custom_short_url=None):
		short_url = custom_short_url if custom_short_url else ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		creation_date = datetime.now()
		expiration_date = creation_date + timedelta(days=30)
		url = URL(original_url, short_url, creation_date, expiration_date, 0)
		self.urls[short_url] = url
		return short_url

	def get_original_url(self, short_url):
		url = self.urls.get(short_url)
		if url and url.expiration_date > datetime.now():
			url.click_count += 1
			return url.original_url
		return None

	def delete_expired_urls(self):
		expired_urls = [short_url for short_url, url in self.urls.items() if url.expiration_date < datetime.now()]
		for short_url in expired_urls:
			del self.urls[short_url]

