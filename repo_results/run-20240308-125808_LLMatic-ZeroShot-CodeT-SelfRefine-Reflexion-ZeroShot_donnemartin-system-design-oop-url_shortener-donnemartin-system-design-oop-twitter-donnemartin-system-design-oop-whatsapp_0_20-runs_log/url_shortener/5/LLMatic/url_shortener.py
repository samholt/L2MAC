import requests
import string
import random
import datetime

class UrlShortener:
	def __init__(self):
		self.url_dict = {}
		self.expiration_dict = {}

	def validate_url(self, url):
		try:
			response = requests.get(url)
			return response.status_code == 200
		except:
			return False

	def generate_short_url(self, url):
		short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		while short_url in self.url_dict:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		self.url_dict[short_url] = url
		return short_url

	def create_custom_short_url(self, custom_url, url):
		if custom_url not in self.url_dict:
			self.url_dict[custom_url] = url
			return custom_url
		else:
			return None

	def set_expiration(self, short_url, expiration_date):
		if short_url in self.url_dict:
			self.expiration_dict[short_url] = datetime.datetime.strptime(expiration_date, '%Y-%m-%d %H:%M:%S')
			return 'Expiration date set'
		else:
			return 'Short URL does not exist'

	def redirect_to_original_url(self, short_url):
		if short_url in self.url_dict:
			if short_url in self.expiration_dict and datetime.datetime.now() > self.expiration_dict[short_url]:
				return None
			else:
				return self.url_dict[short_url]
		else:
			return None

	def get_all_urls(self):
		return self.url_dict

	def delete_url(self, url_id):
		if url_id in self.url_dict:
			del self.url_dict[url_id]
		if url_id in self.expiration_dict:
			del self.expiration_dict[url_id]
