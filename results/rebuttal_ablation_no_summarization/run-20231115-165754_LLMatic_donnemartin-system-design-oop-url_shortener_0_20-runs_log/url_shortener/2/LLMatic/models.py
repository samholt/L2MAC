class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password


class URL:
	def __init__(self, original_url, shortened_url, user, expiration_date=None):
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user = user
		self.expiration_date = expiration_date


class Click:
	def __init__(self, url, datetime, location):
		self.url = url
		self.datetime = datetime
		self.location = location
