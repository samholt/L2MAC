from user import User


class Admin(User):
	def __init__(self, username, password, shortener, users):
		# Initialize the admin
		super().__init__(username, password, shortener)
		self.users = users

	def view_all_urls(self):
		# View all URLs
		return self.shortener.url_mapping

	def delete_url(self, short_url):
		# Delete a URL
		if short_url in self.shortener.url_mapping:
			del self.shortener.url_mapping[short_url]
			return True
		return False

	def delete_user(self, user):
		# Delete a user
		if user in self.users:
			del self.users[user]
			return True
		return False

	def monitor_system(self):
		# Monitor the system
		return self.shortener.click_data
