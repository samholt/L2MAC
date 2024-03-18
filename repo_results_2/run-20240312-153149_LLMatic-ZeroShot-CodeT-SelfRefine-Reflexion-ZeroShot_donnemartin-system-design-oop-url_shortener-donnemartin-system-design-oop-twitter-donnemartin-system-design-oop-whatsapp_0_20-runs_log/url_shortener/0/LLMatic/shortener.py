import hashlib
import requests
from models import Click, URL
from datetime import datetime, timedelta


class Shortener:
	def __init__(self):
		self.urls = {}
		self.clicks = []

	def shorten_url(self, url, custom_short_link=None, user='admin', expiration_days=30):
		if custom_short_link:
			short_url = custom_short_link
		else:
			short_url = hashlib.md5(url.encode()).hexdigest()[:10]
		expirationDate = datetime.now() + timedelta(days=expiration_days)
		self.urls[short_url] = URL(original_url=url, short_url=short_url, user=user, expirationDate=expirationDate)
		return short_url

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except requests.exceptions.RequestException:
			return False

	def record_click(self, short_url, location):
		click = Click(timestamp=datetime.now(), location=location, short_url=short_url)
		self.clicks.append(click)

	def get_clicks(self, short_url):
		return [click for click in self.clicks if click.short_url == short_url]
