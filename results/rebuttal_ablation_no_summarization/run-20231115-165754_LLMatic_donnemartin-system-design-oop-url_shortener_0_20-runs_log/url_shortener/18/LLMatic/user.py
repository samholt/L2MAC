class User:
	def __init__(self, username, password, shortener):
		# Initialize the user
		self.username = username
		self.password = password
		self.urls = {}
		self.shortener = shortener

	def create_account(self):
		# Create an account for the user
		return {'username': self.username, 'password': self.password}

	def view_urls(self):
		# View the user's URLs
		return self.urls

	def edit_url(self, short_url, new_url):
		# Edit a URL
		if short_url in self.urls:
			self.urls[short_url] = new_url
			return True
		return False

	def delete_url(self, short_url):
		# Delete a URL
		if short_url in self.urls:
			del self.urls[short_url]
			return True
		return False

	def view_analytics(self):
		# View the user's analytics
		analytics = {}
		for short_url in self.urls:
			analytics[short_url] = self.shortener.get_click_data(short_url)
		return analytics

	def set_expiration(self, short_url, expiration_date):
		# Set a URL's expiration date
		self.shortener.set_expiration(short_url, expiration_date)
