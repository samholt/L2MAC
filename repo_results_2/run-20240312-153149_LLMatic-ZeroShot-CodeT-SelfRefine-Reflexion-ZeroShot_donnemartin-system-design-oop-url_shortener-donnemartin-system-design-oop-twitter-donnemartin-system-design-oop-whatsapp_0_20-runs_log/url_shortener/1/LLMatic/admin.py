from user import User

class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def view_all_urls(self, users_db):
		all_urls = {}
		for user in users_db.values():
			all_urls.update(user.urls)
		return all_urls

	def delete_url(self, url, users_db):
		for user in users_db.values():
			if url in user.urls:
				del user.urls[url]
				return 'URL deleted successfully'
		return {'error': 'URL not found'}

	def delete_user(self, username, users_db):
		if username in users_db:
			del users_db[username]
			return 'User deleted successfully'
		return {'error': 'User not found'}

	def view_system_performance(self, users_db):
		performance = {'total_users': len(users_db), 'total_urls': sum(len(user.urls) for user in users_db.values())}
		return performance
