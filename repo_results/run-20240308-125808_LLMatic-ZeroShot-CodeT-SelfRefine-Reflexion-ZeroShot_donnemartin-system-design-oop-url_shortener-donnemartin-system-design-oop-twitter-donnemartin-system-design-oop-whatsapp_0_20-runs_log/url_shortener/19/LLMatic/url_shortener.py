import string
import random
from urllib.parse import urlparse
from database import Database
from datetime import datetime, timedelta

class URLShortener:
	def __init__(self, db: Database):
		self.db = db

	def validate_url(self, url: str) -> bool:
		try:
			result = urlparse(url)
			return all([result.scheme, result.netloc])
		except ValueError:
			return False

	def generate_short_url(self, length=6) -> str:
		characters = string.ascii_letters + string.digits
		short_url = ''.join(random.choice(characters) for _ in range(length))
		while self.db.get('urls', short_url):
			short_url = ''.join(random.choice(characters) for _ in range(length))
		return short_url

	def store_url(self, original_url: str, short_url: str, expiration_date: datetime):
		self.db.insert('urls', short_url, {'url': original_url, 'expiration_date': expiration_date})

	def shorten_url(self, original_url: str, expiration_date: datetime, custom_short_url: str = None):
		if not self.validate_url(original_url):
			return 'Invalid URL'
		if custom_short_url:
			if self.db.get('urls', custom_short_url):
				return 'Custom short URL already in use'
			self.store_url(original_url, custom_short_url, expiration_date)
			return custom_short_url
		short_url = self.generate_short_url()
		self.store_url(original_url, short_url, expiration_date)
		return short_url

	def get_original_url(self, short_url: str):
		url_data = self.db.get('urls', short_url)
		if url_data and (url_data['expiration_date'] is None or url_data['expiration_date'] > datetime.now()):
			return url_data['url']
		return None
