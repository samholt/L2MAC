from datetime import datetime


class User:
	users_db = {}

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = []

	@classmethod
	def save_to_db(cls, user):
		cls.users_db[user.username] = user

	@classmethod
	def find_by_username(cls, username):
		return cls.users_db.get(username, None)

	def add_url(self, url):
		self.urls.append(url)

	def remove_url(self, url):
		self.urls.remove(url)

	def edit_url(self, old_url, new_url):
		for url in self.urls:
			if url.shortened_url == old_url:
				url.original_url = new_url
				return True
		return False

	def delete_url(self, url_to_delete):
		for url in self.urls:
			if url.shortened_url == url_to_delete:
				self.urls.remove(url)
				return True
		return False

	def get_analytics(self, url_to_analyze):
		for url in self.urls:
			if url.shortened_url == url_to_analyze:
				return {'clicks': url.clicks, 'creation_date': url.creation_date, 'expiration_date': url.expiration_date}
		return None


class URL:
	urls_db = {}

	def __init__(self, original_url, shortened_url, user, creation_date, expiration_date):
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user = user
		self.creation_date = creation_date
		self.expiration_date = expiration_date
		self.clicks = 0

	@classmethod
	def save_to_db(cls, url):
		cls.urls_db[url.shortened_url] = url

	@classmethod
	def find_by_short_url(cls, short_url):
		return cls.urls_db.get(short_url, None)

	def click(self):
		self.clicks += 1


class Admin(User):
	def __init__(self, username, password):
		super().__init__(username, password)

	def get_all_urls(self):
		return list(URL.urls_db.values())

	def delete_url(self, url_to_delete):
		url = URL.find_by_short_url(url_to_delete)
		if url:
			URL.urls_db.pop(url_to_delete)
			return True
		return False

	def delete_user(self, username):
		user = User.find_by_username(username)
		if user:
			User.users_db.pop(username)
			return True
		return False

	def get_system_stats(self):
		total_urls = len(URL.urls_db)
		total_users = len(User.users_db)
		total_clicks = sum(url.clicks for url in URL.urls_db.values())
		return {'total_urls': total_urls, 'total_users': total_users, 'total_clicks': total_clicks}
