class AdminDashboard:
	def __init__(self, url_database, user_database):
		self.url_database = url_database
		self.user_database = user_database

	def view_all_urls(self):
		return self.url_database

	def delete_url(self, short_url):
		if short_url in self.url_database:
			del self.url_database[short_url]

	def delete_user(self, username):
		if username in self.user_database:
			del self.user_database[username]

	def monitor_system(self, analytics):
		return analytics
