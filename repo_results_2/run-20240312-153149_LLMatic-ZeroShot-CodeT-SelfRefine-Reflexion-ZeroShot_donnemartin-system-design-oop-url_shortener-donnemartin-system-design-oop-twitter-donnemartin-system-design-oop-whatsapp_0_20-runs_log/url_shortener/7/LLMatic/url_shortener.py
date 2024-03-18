import requests
import string
import random
import datetime

# Mock database
DATABASE = {}

class URLShortener:
	def __init__(self):
		self.DATABASE = DATABASE

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except:
			return False

	def generate_short_url(self, url, expiration_days=30):
		if url in self.DATABASE:
			return self.DATABASE[url]['short_url']
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			expiration_date = datetime.datetime.now() + datetime.timedelta(days=expiration_days)
			self.DATABASE[url] = {'short_url': short_url, 'expiration_date': expiration_date}
			return short_url

	def custom_short_link(self, url, custom_link, expiration_days=30):
		if custom_link in [data['short_url'] for data in self.DATABASE.values()]:
			return None
		else:
			expiration_date = datetime.datetime.now() + datetime.timedelta(days=expiration_days)
			self.DATABASE[url] = {'short_url': custom_link, 'expiration_date': expiration_date}
			return custom_link

	def get_original_url(self, short_url):
		for url, data in self.DATABASE.items():
			if data['short_url'] == short_url:
				if datetime.datetime.now() <= data['expiration_date']:
					return url
		return None

