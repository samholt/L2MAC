class Admin:
	def __init__(self, url_shortener):
		# Initialize Admin with URLShortener
		self.url_shortener = url_shortener

	def view_all_urls(self):
		# View all URLs in the system
		return self.url_shortener.urls

	def delete_url(self, short_url):
		# Delete a URL from the system
		if short_url in self.url_shortener.urls:
			del self.url_shortener.urls[short_url]
			del self.url_shortener.analytics[short_url]

	def delete_user(self, username):
		# Delete a user from the system
		if username in self.url_shortener.users:
			del self.url_shortener.users[username]

	def monitor_system(self):
		# Monitor the system
		return {
			'users': len(self.url_shortener.users),
			'urls': len(self.url_shortener.urls),
			'clicks': sum([data['clicks'] for data in self.url_shortener.analytics.values()])
		}
