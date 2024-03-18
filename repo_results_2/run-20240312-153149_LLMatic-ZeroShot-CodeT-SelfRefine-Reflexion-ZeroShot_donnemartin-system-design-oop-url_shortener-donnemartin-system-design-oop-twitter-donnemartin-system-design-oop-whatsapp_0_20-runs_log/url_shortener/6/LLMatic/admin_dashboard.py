from url_shortener import validate_url
from user_accounts import UserAccounts
from analytics import analytics_db


class AdminDashboard:
	def __init__(self):
		# Class for managing the admin dashboard
		self.user_accounts = UserAccounts()

	def view_all_urls(self):
		# Method to view all URLs in the system
		all_urls = []
		for user in self.user_accounts.users.values():
			all_urls.extend(user['urls'])
		return all_urls

	def delete_url(self, username, url):
		# Method to delete a URL associated with a user account
		if username in self.user_accounts.users:
			if url in self.user_accounts.users[username]['urls']:
				self.user_accounts.users[username]['urls'].remove(url)
				return True
		return False

	def delete_user(self, username):
		# Method to delete a user account
		if username in self.user_accounts.users:
			del self.user_accounts.users[username]
			return True
		return False

	def view_system_performance(self):
		# Method to view system performance metrics
		return len(self.view_all_urls()), len(self.user_accounts.users)

	def view_analytics(self, url):
		# Method to view analytics for a specific URL
		return analytics_db.get(url, [])
