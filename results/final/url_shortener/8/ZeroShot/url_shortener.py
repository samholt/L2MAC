import string
import random
from datetime import datetime, timedelta

class URLShortener:
	def __init__(self):
		self.urls = {}

	def shorten_url(self, url, custom_alias=None, user_id=None, expiration_date=None):
		if custom_alias:
			short_url = custom_alias
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		self.urls[short_url] = {'url': url, 'user_id': user_id, 'clicks': 0, 'click_data': [], 'expiration_date': expiration_date}
		return short_url

	def get_original_url(self, short_url):
		url_data = self.urls.get(short_url)
		if url_data and (not url_data['expiration_date'] or datetime.now() < url_data['expiration_date']):
			url_data['clicks'] += 1
			url_data['click_data'].append({'click_time': datetime.now().isoformat()})
			return url_data['url']
		else:
			return None

	def get_all_urls(self):
		return self.urls
