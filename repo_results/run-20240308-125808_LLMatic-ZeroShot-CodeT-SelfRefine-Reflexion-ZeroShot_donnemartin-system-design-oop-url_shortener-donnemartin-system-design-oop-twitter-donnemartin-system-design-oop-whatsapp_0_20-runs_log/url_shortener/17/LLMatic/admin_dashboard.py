class AdminDashboard:
	def __init__(self, url_db, user_accounts):
		self.url_db = url_db
		self.user_accounts = user_accounts

	def view_all_urls(self):
		return self.url_db

	def delete_url(self, short_url):
		if short_url in self.url_db:
			del self.url_db[short_url]
			return 'URL deleted successfully.'
		return 'URL does not exist.'

	def delete_user(self, username):
		if username in self.user_accounts.users:
			del self.user_accounts.users[username]
			return 'User deleted successfully.'
		return 'User does not exist.'

	def monitor_system(self):
		# For simplicity, we'll just return the number of URLs and users
		url_count = len(self.url_db)
		user_count = len(self.user_accounts.users)
		return {'url_count': url_count, 'user_count': user_count}
