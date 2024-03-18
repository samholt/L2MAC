import psutil
from url_shortener import URLShortener, DATABASE as URL_DATABASE
from user_accounts import UserAccounts, USER_DB
from analytics import Analytics, ANALYTICS_DB


class AdminDashboard:
	def __init__(self):
		self.url_shortener = URLShortener()
		self.user_accounts = UserAccounts()
		self.analytics = Analytics()

	def view_all_urls(self):
		return URL_DATABASE

	def view_user_accounts(self):
		return USER_DB

	def delete_url(self, short_url):
		original_url = self.url_shortener.get_original_url(short_url)
		if original_url:
			del URL_DATABASE[original_url]
			return True
		else:
			return False

	def delete_user(self, username):
		if username in USER_DB:
			del USER_DB[username]
			return True
		else:
			return False

	def system_performance(self):
		cpu_usage = psutil.cpu_percent()
		memory_usage = psutil.virtual_memory().percent
		return {'cpu_usage': cpu_usage, 'memory_usage': memory_usage}

	def view_analytics(self):
		return ANALYTICS_DB
