class AdminDashboard:
	def __init__(self):
		self.users = {}
		self.urls = {}

	def view_all_urls(self):
		return self.urls

	def delete_url(self, url):
		if url in self.urls:
			del self.urls[url]
		return self.urls

	def delete_user(self, user):
		if user in self.users:
			del self.users[user]
		return self.users

	def monitor_system(self):
		return {'users': len(self.users), 'urls': len(self.urls)}
