from user_accounts import UserAccounts
from analytics import Analytics

class AdminDashboard:
	def __init__(self):
		self.user_accounts = UserAccounts()
		self.analytics = Analytics()

	def view_all_urls(self):
		all_urls = []
		for user in self.user_accounts.users.values():
			all_urls.extend(user['urls'])
		return all_urls

	def delete_url(self, url):
		for user in self.user_accounts.users.values():
			if url in user['urls']:
				user['urls'].remove(url)
				return 'URL deleted successfully.'
		return 'URL not found.'

	def delete_user(self, username):
		if username in self.user_accounts.users:
			del self.user_accounts.users[username]
			return 'User deleted successfully.'
		return 'User not found.'

	def view_analytics(self):
		return self.analytics.data
