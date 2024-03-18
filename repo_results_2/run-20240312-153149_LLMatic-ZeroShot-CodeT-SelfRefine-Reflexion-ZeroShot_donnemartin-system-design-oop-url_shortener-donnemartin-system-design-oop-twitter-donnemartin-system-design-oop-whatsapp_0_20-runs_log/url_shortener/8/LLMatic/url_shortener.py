import string
import random
from datetime import datetime
import re


class URLShortener:
	def __init__(self):
		# Initialize URLShortener with empty dictionaries for URLs, analytics, and users
		self.urls = {}
		self.analytics = {}
		self.users = {}

	def shorten_url(self, long_url, username=None, expiration=None):
		# Shorten the provided URL and store it
		if not re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', long_url):
			return None
		short_url = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
		self.urls[short_url] = {'long_url': long_url, 'username': username, 'expiration': expiration}
		self.analytics[short_url] = {'clicks': 0, 'click_details': []}
		return short_url

	def get_long_url(self, short_url):
		# Get the original URL associated with the short URL
		if short_url in self.urls:
			if self.urls[short_url]['expiration'] and datetime.now() > self.urls[short_url]['expiration']:
				return None
			self.analytics[short_url]['clicks'] += 1
			self.analytics[short_url]['click_details'].append({'clicked_at': datetime.now().isoformat()})
			return self.urls[short_url]['long_url']
		return None

	def edit_url(self, short_url, new_long_url, username):
		# Edit a URL
		if short_url in self.urls and self.urls[short_url]['username'] == username:
			self.urls[short_url]['long_url'] = new_long_url

	def delete_url(self, short_url, username):
		# Delete a URL
		if short_url in self.urls and self.urls[short_url]['username'] == username:
			del self.urls[short_url]
			del self.analytics[short_url]

	def get_analytics(self, short_url):
		# Get analytics of a URL
		if short_url in self.analytics:
			return self.analytics[short_url]
		return None

	def add_user(self, user):
		# Add a user
		self.users[user.username] = user
