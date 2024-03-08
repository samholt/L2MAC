from shortener import Shortener
from user import User


class Admin:
	def __init__(self, shortener: Shortener, user: User):
		self.shortener = shortener
		self.user = user

	def view_all_urls(self):
		return self.shortener.url_map

	def delete_url(self, short_url):
		if short_url in self.shortener.url_map:
			del self.shortener.url_map[short_url]
			return True
		return False

	def delete_user(self, username):
		if username in self.user.users:
			del self.user.users[username]
			return True
		return False

	def monitor_system(self):
		return {
			'users': len(self.user.users),
			'urls': len(self.shortener.url_map)
		}
