from user import User


class Admin(User):
	def __init__(self, username):
		super().__init__(username)
		self.all_urls = {}
		self.all_users = {}

	def add_user(self, user):
		self.all_users[user.username] = user

	def view_all_urls(self):
		for user in self.all_users.values():
			self.all_urls.update(user.view_urls())
		return self.all_urls

	def delete_url(self, short_url):
		for user in self.all_users.values():
			user.delete_url(short_url)
		if short_url in self.all_urls:
			del self.all_urls[short_url]

	def delete_user(self, username):
		if username in self.all_users:
			del self.all_users[username]

	def monitor_system(self, analytics):
		system_analytics = {}
		for url in self.all_urls:
			system_analytics[url] = analytics.retrieve(url)
		return system_analytics
