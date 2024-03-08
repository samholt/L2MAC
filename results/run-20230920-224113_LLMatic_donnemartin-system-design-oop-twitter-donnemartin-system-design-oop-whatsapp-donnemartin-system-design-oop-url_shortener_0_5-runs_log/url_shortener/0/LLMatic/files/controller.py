import hashlib
import base64
from datetime import datetime, timedelta
from models import URL


class URLController:
	def __init__(self):
		self.urls = {}

	def create_short_url(self, original_url):
		# Generate a unique short URL by hashing the original URL
		short_url = base64.urlsafe_b64encode(hashlib.sha256(original_url.encode()).digest()).decode()[:10]
		url = URL(original_url, short_url)
		self.urls[short_url] = url
		return short_url

	def get_original_url(self, short_url):
		# Get the original URL from the short URL
		url = self.urls.get(short_url)
		if url:
			url.increment_click_count()
			return url.original_url
		return None

	def get_click_stats(self, short_url):
		# Get the click stats for a short URL
		url = self.urls.get(short_url)
		if url:
			return url.click_count
		return None

	def delete_expired_urls(self, expiry_days=30):
		# Delete URLs that are older than the expiry days
		expiry_date = datetime.now() - timedelta(days=expiry_days)
		expired_urls = [short_url for short_url, url in self.urls.items() if url.creation_date < expiry_date]
		for short_url in expired_urls:
			del self.urls[short_url]

