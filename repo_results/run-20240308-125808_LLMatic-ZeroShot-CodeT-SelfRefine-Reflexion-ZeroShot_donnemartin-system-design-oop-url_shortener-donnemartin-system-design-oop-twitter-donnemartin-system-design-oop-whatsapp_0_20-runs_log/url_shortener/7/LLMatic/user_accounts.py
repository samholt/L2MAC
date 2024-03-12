class UserAccount:
	def __init__(self):
		self.users = {}

	def create_account(self, username, password):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = {'password': password, 'urls': []}
		return 'Account created successfully.'

	def view_urls(self, username):
		if username not in self.users:
			return 'User not found.'
		return self.users[username]['urls']

	def add_url(self, username, url):
		if username not in self.users:
			return 'User not found.'
		self.users[username]['urls'].append(url)
		return 'URL added successfully.'

	def delete_url(self, username, url):
		if username not in self.users:
			return 'User not found.'
		if url not in self.users[username]['urls']:
			return 'URL not found.'
		self.users[username]['urls'].remove(url)
		return 'URL removed successfully.'

	def view_analytics(self, username):
		if username not in self.users:
			return 'User not found.'
		analytics = []
		for url in self.users[username]['urls']:
			analytics.append({'url': url, 'clicks': 0})
		return analytics
