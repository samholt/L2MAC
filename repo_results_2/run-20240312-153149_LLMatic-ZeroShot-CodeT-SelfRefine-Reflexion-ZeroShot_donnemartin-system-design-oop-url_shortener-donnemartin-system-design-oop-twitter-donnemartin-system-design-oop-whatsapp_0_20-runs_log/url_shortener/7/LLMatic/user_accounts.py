import string
import random

# Mock database
USER_DB = {}

class UserAccounts:
	def __init__(self):
		self.USER_DB = USER_DB

	def create_account(self, username):
		if username in self.USER_DB:
			return None
		else:
			self.USER_DB[username] = {'urls': {}}
			return self.USER_DB[username]

	def get_user_urls(self, username):
		user = self.USER_DB.get(username)
		if user:
			return user['urls']
		else:
			return None

	def add_url_to_user(self, username, original_url, short_url):
		user = self.USER_DB.get(username)
		if user:
			user['urls'][short_url] = original_url
			return True
		else:
			return False

	def delete_url_from_user(self, username, short_url):
		user = self.USER_DB.get(username)
		if user and short_url in user['urls']:
			del user['urls'][short_url]
			return True
		else:
			return False

	def get_user_analytics(self, username, analytics):
		user = self.USER_DB.get(username)
		if user:
			user_urls = user['urls']
			analytics_data = {}
			for short_url in user_urls:
				analytics_data[short_url] = analytics.get_analytics(short_url) if analytics else None
			return analytics_data
		else:
			return None
