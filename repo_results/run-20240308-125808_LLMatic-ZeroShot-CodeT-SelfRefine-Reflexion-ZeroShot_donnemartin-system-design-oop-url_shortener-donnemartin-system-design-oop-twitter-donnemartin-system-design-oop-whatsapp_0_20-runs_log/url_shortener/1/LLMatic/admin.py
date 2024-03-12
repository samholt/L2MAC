from user import User, users


class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def view_all_urls(self):
		all_urls = {}
		for user in users.values():
			all_urls.update(user.view_urls())
		return all_urls

	def delete_url(self, shortened_url):
		for user in users.values():
			if shortened_url in user.urls:
				del user.urls[shortened_url]
				break

	def delete_user(self, username):
		if username in users:
			del users[username]

	def view_system_analytics(self):
		all_analytics = {}
		for user in users.values():
			all_analytics[user.username] = user.view_analytics()
		return all_analytics
