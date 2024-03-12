from user_accounts import UserAccount
from database import url_db
from analytics import get_analytics_db


class AdminDashboard:
	def __init__(self):
		self.user_account = UserAccount()

	def view_all_urls(self):
		return url_db

	def delete_url(self, short_url):
		if short_url in url_db:
			del url_db[short_url]
			return 'URL deleted successfully'
		return 'URL does not exist'

	def delete_user(self, username):
		if username in self.user_account.accounts:
			del self.user_account.accounts[username]
			return 'User deleted successfully'
		return 'Username does not exist'

	def view_system_performance(self):
		return get_analytics_db()

