from models import User, URL
import random
import string


class URLShortener:
	def __init__(self):
		self.users = {}
		self.urls = {}

	def create_user(self, username: str, password: str):
		user = User(username, password)
		self.users[username] = user
		return user

	def create_url(self, original_url: str, user: User, custom_short_url: str = None):
		if custom_short_url:
			shortened_url = custom_short_url
		else:
			shortened_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		url = URL(original_url, shortened_url, user)
		self.urls[shortened_url] = url
		user.add_url(original_url, shortened_url)
		return url

	def get_url(self, shortened_url: str):
		return self.urls.get(shortened_url)

	def delete_url(self, shortened_url: str, user: User):
		if shortened_url in user.urls:
			user.delete_url(shortened_url)
			if shortened_url in self.urls:
				del self.urls[shortened_url]
