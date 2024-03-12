from user import User


class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.all_urls = {}
		self.all_users = {}

	def view_all_urls(self):
		return self.all_urls

	def delete_url(self, url):
		if url in self.all_urls:
			del self.all_urls[url]
		else:
			return 'URL not found', 404

	def delete_user(self, user):
		if user in self.all_users:
			del self.all_users[user]
		else:
			return 'User not found', 404

	def monitor_system(self):
		# In a real-world application, this method would return system performance and analytics
		# Here, we'll just print a message
		print('Monitoring system performance and analytics')
