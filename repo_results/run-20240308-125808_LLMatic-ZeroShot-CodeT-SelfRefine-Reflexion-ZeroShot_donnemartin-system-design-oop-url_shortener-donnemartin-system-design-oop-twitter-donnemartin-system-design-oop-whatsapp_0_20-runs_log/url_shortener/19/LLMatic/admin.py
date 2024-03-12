from database import Database
from user import User
from url_shortener import URLShortener
from datetime import datetime, timedelta

class Admin:
	def __init__(self):
		self.db = Database()
		self.user = User()
		self.url_shortener = URLShortener(self.db)

	def get_all_urls(self):
		return self.db.urls

	def delete_url(self, short_url):
		self.db.delete('urls', short_url)

	def delete_user(self, username):
		self.user.delete_user(username)

	def get_system_performance(self):
		# For simplicity, we'll just return the number of users and URLs
		return {'users': len(self.db.users), 'urls': len(self.db.urls)}
