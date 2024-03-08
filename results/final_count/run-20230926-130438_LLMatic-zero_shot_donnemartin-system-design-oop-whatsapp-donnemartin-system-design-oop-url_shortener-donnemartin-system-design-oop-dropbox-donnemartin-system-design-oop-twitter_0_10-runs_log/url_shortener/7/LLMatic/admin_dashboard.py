from user_accounts import UserAccount
from url_shortener import generate_short_url, validate_url


class AdminDashboard:
	def __init__(self):
		self.user_account = UserAccount()

	def view_all_urls(self):
		all_urls = []
		for user in self.user_account.users:
			all_urls.extend(self.user_account.users[user])
		return all_urls

	def delete_url(self, username, url):
		return self.user_account.delete_url(username, url)

	def delete_user(self, username):
		if username in self.user_account.users:
			del self.user_account.users[username]
			return 'User deleted successfully.'
		return 'Username does not exist.'

	def monitor_system(self):
		# For simplicity, we will just return the number of users and total URLs
		total_users = len(self.user_account.users)
		total_urls = sum(len(self.user_account.users[user]) for user in self.user_account.users)
		return {'total_users': total_users, 'total_urls': total_urls}
