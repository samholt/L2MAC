class UserAccount:
	def __init__(self):
		self.users = {}

	def create_account(self, username):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = {'urls': []}
		return 'Account created successfully.'

	def view_urls(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		return self.users[username]['urls']

	def edit_url(self, username, old_url, new_url):
		if username not in self.users:
			return 'Username does not exist.'
		if old_url not in self.users[username]['urls']:
			return 'URL does not exist.'
		self.users[username]['urls'].remove(old_url)
		self.users[username]['urls'].append(new_url)
		return 'URL edited successfully.'

	def delete_url(self, username, url):
		if username not in self.users:
			return 'Username does not exist.'
		if url not in self.users[username]['urls']:
			return 'URL does not exist.'
		self.users[username]['urls'].remove(url)
		return 'URL deleted successfully.'

	def view_analytics(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		return {url['url']: url['analytics'] for url in self.users[username]['urls'] if 'analytics' in url}
