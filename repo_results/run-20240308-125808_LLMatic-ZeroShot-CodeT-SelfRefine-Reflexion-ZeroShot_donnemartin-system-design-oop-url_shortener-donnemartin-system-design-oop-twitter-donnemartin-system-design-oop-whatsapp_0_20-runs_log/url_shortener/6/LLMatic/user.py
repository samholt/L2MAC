class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = {}

	def create_account(self):
		# In a real-world application, this method would interact with a database
		# Here, we'll just print a message
		print(f'Account created for {self.username}')

	def view_urls(self):
		return self.urls

	def edit_url(self, old_url, new_url):
		if old_url in self.urls:
			self.urls[new_url] = self.urls.pop(old_url)
		else:
			return 'URL not found', 404

	def delete_url(self, url):
		if url in self.urls:
			del self.urls[url]
		else:
			return 'URL not found', 404
