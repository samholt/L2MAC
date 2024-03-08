class User:
	def __init__(self, id, username, password, is_admin=False):
		self.id = id
		self.username = username
		self.password = password
		self.is_admin = is_admin


class URL:
	def __init__(self, id, original_url, shortened_url, user_id, expiration_date):
		self.id = id
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user_id = user_id
		self.expiration_date = expiration_date


class Click:
	def __init__(self, id, url_id, timestamp, location):
		self.id = id
		self.url_id = url_id
		self.timestamp = timestamp
		self.location = location

