from datetime import datetime
class MockDB:
	def __init__(self):
		self.db = {}
		self.analytics = {}
		self.accounts = {}

	def add_url(self, url, custom_short_link=None, username=None):
		if custom_short_link and custom_short_link in self.db:
			return None
		
		short_url = custom_short_link if custom_short_link else self.generate_short_url()
		self.db[short_url] = url
		self.analytics[short_url] = {'clicks': 0, 'timestamps': []}
		if username:
			if username not in self.accounts:
				self.accounts[username] = {'password': '', 'urls': {}}
			self.accounts[username]['urls'][short_url] = url
		return short_url

	def get_url(self, short_url):
		if short_url in self.db:
			self.analytics[short_url]['clicks'] += 1
			self.analytics[short_url]['timestamps'].append(str(datetime.now()))
			return self.db[short_url]
		return None

	def get_analytics(self, short_url):
		return self.analytics.get(short_url)

	def get_user_analytics(self, username):
		if username in self.accounts:
			user_urls = self.accounts[username]['urls']
			return {url: self.analytics[url] for url in user_urls if url in self.analytics}
		return None

	def create_account(self, username, password):
		if username not in self.accounts:
			self.accounts[username] = {'password': password, 'urls': {}}
			return 'Account created'
		return 'Account already exists'

	def get_user_urls(self, username):
		return self.accounts.get(username, {}).get('urls', {})

	def update_url(self, username, old_short_url, new_short_url):
		if username in self.accounts and old_short_url in self.accounts[username]['urls']:
			self.accounts[username]['urls'][new_short_url] = self.accounts[username]['urls'].pop(old_short_url)
			return 'URL updated'
		return 'URL not found'

	def delete_url(self, username, short_url):
		if username in self.accounts and short_url in self.accounts[username]['urls']:
			del self.accounts[username]['urls'][short_url]
			return 'URL deleted'
		return 'URL not found'

	def delete_admin(self, username, short_url):
		if username in self.accounts:
			if short_url:
				if short_url in self.accounts[username]['urls']:
					del self.accounts[username]['urls'][short_url]
					return 'URL deleted'
				return 'URL not found'
			else:
				del self.accounts[username]
				return 'Account deleted'
		return 'Account not found'

	def get_admin_dashboard(self):
		return self.accounts

	def generate_short_url(self):
		return str(len(self.db))

