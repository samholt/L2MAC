from user import User
from shortener import Shortener


class Admin(User):
	def __init__(self, username, shortener):
		super().__init__(username)
		self.shortener = shortener

	def view_all_urls(self):
		return {short_url: url_data['url'] for short_url, url_data in self.shortener.url_mapping.items()}

	def delete_url(self, short_url):
		if short_url in self.shortener.url_mapping:
			del self.shortener.url_mapping[short_url]
		return self.shortener.url_mapping

	def delete_user(self, username):
		user = User(username)
		user.urls = {}
		self.shortener.url_mapping = {k: v for k, v in self.shortener.url_mapping.items() if v['username'] != username}
		return user.urls

	def monitor_system(self, analytics):
		total_clicks = 0
		for data in analytics.analytics_data.values():
			total_clicks += data['clicks']
		return {'total_urls': len(self.shortener.url_mapping), 'total_clicks': total_clicks}

