from database import Database


class Admin:
	def __init__(self, database):
		self.database = database

	def view_all_urls(self):
		return list(self.database.urls.values())

	def delete_url(self, short_url):
		if short_url in self.database.urls:
			del self.database.urls[short_url]
			return True
		return False

	def delete_user(self, username):
		if username in self.database.users:
			del self.database.users[username]
			return True
		return False

	def monitor_system(self):
		user_count = len(self.database.users)
		url_count = len(self.database.urls)
		return {'user_count': user_count, 'url_count': url_count}
