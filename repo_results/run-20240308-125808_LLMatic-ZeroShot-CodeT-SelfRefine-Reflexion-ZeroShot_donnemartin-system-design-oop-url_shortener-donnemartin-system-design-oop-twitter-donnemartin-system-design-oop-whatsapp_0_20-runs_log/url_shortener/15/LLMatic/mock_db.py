import random
import string
from datetime import datetime


class MockDB:
	def __init__(self):
		self.data = {}
		self.users = {}
		self.analytics = {}

	def add_url(self, url, custom_short_link=None, expiration_date=None):
		if custom_short_link and custom_short_link in self.data:
			return None
		short_url = custom_short_link if custom_short_link else ''.join(random.choice(string.ascii_letters) for _ in range(5))
		self.data[short_url] = {'url': url, 'expiration_date': expiration_date}
		self.analytics[short_url] = {'clicks': 0, 'click_data': []}
		return short_url

	def get_url(self, short_url):
		url_data = self.data.get(short_url)
		if url_data:
			self.analytics[short_url]['clicks'] += 1
			self.analytics[short_url]['click_data'].append({'time': datetime.now().isoformat(), 'location': 'Unknown'})
		return url_data

	def delete_url(self, short_url):
		if short_url in self.data:
			del self.data[short_url]
		if short_url in self.analytics:
			del self.analytics[short_url]

	def get_analytics(self, short_url):
		return self.analytics.get(short_url)

	def get_all_analytics(self):
		return self.analytics

	def add_user(self, username, password):
		user_id = ''.join(random.choice(string.ascii_letters) for _ in range(5))
		self.users[user_id] = {'username': username, 'password': password}
		return user_id

	def get_user(self, user_id):
		return self.users.get(user_id)

	def update_user(self, user_id, username, password):
		if user_id in self.users:
			self.users[user_id] = {'username': username, 'password': password}

	def delete_user(self, user_id):
		if user_id in self.users:
			del self.users[user_id]

	def get_admin_data(self):
		return {'users': self.users, 'urls': self.data}
