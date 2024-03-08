class AdminService:
	def __init__(self, url_shortener, user_service):
		self.url_shortener = url_shortener
		self.user_service = user_service

	def get_all_urls(self):
		return self.url_shortener.url_data

	def delete_url(self, short_url):
		if short_url in self.url_shortener.url_data:
			del self.url_shortener.url_data[short_url]
			return 'URL deleted'
		return 'URL not found'

	def delete_user(self, username):
		if username in self.user_service.users:
			del self.user_service.users[username]
			return 'User deleted'
		return 'User not found'
