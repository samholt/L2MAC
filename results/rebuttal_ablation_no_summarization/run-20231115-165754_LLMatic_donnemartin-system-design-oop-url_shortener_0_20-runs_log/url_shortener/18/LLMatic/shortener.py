import string
import random
import requests
from datetime import datetime


class Shortener:
	def __init__(self):
		# Initialize the shortener
		self.url_mapping = {}
		self.click_data = {}
		self.expiration_data = {}

	def shorten_url(self, url):
		# Shorten a URL
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
		while short_url in self.url_mapping:
			short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
		self.url_mapping[short_url] = url
		self.click_data[short_url] = {'clicks': 0, 'click_data': []}
		return short_url

	def validate_url(self, url):
		# Validate a URL
		try:
			response = requests.get(url)
			return response.status_code == 200
		except:
			return False

	def get_original_url(self, short_url):
		# Get the original URL of a shortened URL
		if short_url in self.expiration_data and datetime.now() > datetime.fromisoformat(self.expiration_data[short_url]):
			return None
		return self.url_mapping.get(short_url, None)

	def track_click(self, short_url, location):
		# Track a click on a shortened URL
		if short_url in self.click_data:
			self.click_data[short_url]['clicks'] += 1
			self.click_data[short_url]['click_data'].append({'time': datetime.now().isoformat(), 'location': location})

	def get_click_data(self, short_url):
		# Get the click data for a shortened URL
		return self.click_data.get(short_url, None)

	def set_expiration(self, short_url, expiration_datetime):
		# Set a URL's expiration date
		self.expiration_data[short_url] = expiration_datetime
