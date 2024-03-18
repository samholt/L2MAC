class User:
	def __init__(self, username, password):
		# Initialize User with username, password, and empty dictionary for URLs
		self.username = username
		self.password = password
		self.urls = {}

	def create_account(self, url_shortener):
		# Create a new account for the user
		url_shortener.add_user(self)

	def view_urls(self):
		# View all URLs of the user
		return self.urls

	def add_url(self, long_url, url_shortener):
		# Add a new URL for the user
		short_url = url_shortener.shorten_url(long_url, self.username)
		self.urls[short_url] = long_url
		return short_url

	def edit_url(self, short_url, new_long_url, url_shortener):
		# Edit a URL of the user
		if short_url in self.urls:
			url_shortener.edit_url(short_url, new_long_url, self.username)
			self.urls[short_url] = new_long_url

	def delete_url(self, short_url, url_shortener):
		# Delete a URL of the user
		if short_url in self.urls:
			url_shortener.delete_url(short_url, self.username)
			del self.urls[short_url]

	def view_analytics(self, short_url, url_shortener):
		# View analytics of a URL of the user
		if short_url in self.urls:
			analytics = url_shortener.get_analytics(short_url)
			if analytics is not None:
				return analytics
		return {'message': 'No analytics available for this URL'}
