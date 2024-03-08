import string
import random
from datetime import datetime
from dataclasses import dataclass


@dataclass
class URL:
	original_url: str
	shortened_url: str
	creation_date: datetime
	expiration_date: datetime
	clicks: int = 0


class URLShortener:
	def __init__(self):
		self.urls = {}

	def generate_short_url(self, original_url: str, expiration_date: datetime) -> str:
		# This method will generate a short URL and store it in the urls dictionary.
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		self.urls[short_url] = URL(original_url, short_url, datetime.now(), expiration_date)
		return short_url

	def get_original_url(self, short_url: str) -> str:
		# This method will return the original URL for a given short URL.
		if short_url in self.urls:
			return self.urls[short_url].original_url
		else:
			return None

	def track_click(self, short_url: str):
		# This method will increment the click count for a given short URL.
		if short_url in self.urls:
			self.urls[short_url].clicks += 1

	def delete_expired_urls(self):
		# This method will delete all expired URLs from the urls dictionary.
		current_time = datetime.now()
		expired_urls = [url for url, url_data in self.urls.items() if url_data.expiration_date < current_time]
		for url in expired_urls:
			self.urls.pop(url)
