from user import User

class Admin(User):
	def __init__(self, username, system):
		super().__init__(username)
		self.system = system

	def view_all_urls(self):
		all_urls = {}
		for user in self.system.users.values():
			all_urls.update(user.get_urls())
		return all_urls

	def delete_url(self, username, short_url):
		if username in self.system.users:
			self.system.users[username].delete_url(short_url)

	def delete_user(self, username):
		if username in self.system.users:
			del self.system.users[username]
			return True
		return False

	def monitor_system(self):
		return {'total_users': len(self.system.users), 'total_urls': sum(len(user.get_urls()) for user in self.system.users.values())}
