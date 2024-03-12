from url_shortener import UrlShortener
from user_account import UserAccount

class AdminDashboard:
	def __init__(self):
		self.url_shortener = UrlShortener()
		self.user_account = UserAccount()

	def view_all_urls(self):
		return self.url_shortener.get_all_urls()

	def delete_url(self, url_id):
		self.url_shortener.delete_url(url_id)
		return 'URL deleted'

	def delete_user(self, user_id):
		self.user_account.delete_user(user_id)
		return 'User deleted'

	def monitor_system(self):
		# Mocking system performance and analytics
		return {'system_performance': 'Good', 'analytics': 'Normal'}
