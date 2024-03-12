from models import User, URL


class Database:
	def __init__(self):
		self.users = {}
		self.urls = {}

	def add_user(self, user: User):
		self.users[user.id] = user

	def get_user(self, user_id: str) -> User:
		return self.users.get(user_id)

	def add_url(self, url: URL):
		self.urls[url.id] = url

	def get_url(self, url_id: str) -> URL:
		return self.urls.get(url_id)

	def get_all_urls(self) -> dict:
		return self.urls

	def delete_url(self, url_id: str):
		self.urls.pop(url_id, None)

	def delete_user(self, user_id: str):
		self.users.pop(user_id, None)

