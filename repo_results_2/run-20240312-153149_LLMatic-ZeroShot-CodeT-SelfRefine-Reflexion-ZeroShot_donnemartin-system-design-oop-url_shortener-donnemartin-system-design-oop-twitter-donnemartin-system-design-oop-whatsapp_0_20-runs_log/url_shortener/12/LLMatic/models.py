from datetime import datetime, timedelta

class User:
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password

	@classmethod
	def create(cls, id, username, password):
		return cls(id, username, password)

	def authenticate(self, username, password):
		return self.username == username and self.password == password

	def get_details(self):
		return {
			'id': self.id,
			'username': self.username,
			'password': self.password
		}

class URL:
	def __init__(self, original_url, shortened_url, user, creation_date=None, expiration_date=None):
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user = user
		self.creation_date = creation_date or datetime.now()
		self.expiration_date = expiration_date or (self.creation_date + timedelta(days=30))

	@classmethod
	def create(cls, original_url, shortened_url, user):
		return cls(original_url, shortened_url, user)

	def get_details(self):
		return {
			'original_url': self.original_url,
			'shortened_url': self.shortened_url,
			'user': self.user.get_details(),
			'creation_date': self.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
			'expiration_date': self.expiration_date.strftime('%Y-%m-%d %H:%M:%S')
		}

	def update_original_url(self, new_url):
		self.original_url = new_url

	def delete(self):
		self.original_url = None
		self.shortened_url = None
		self.user = None
		self.creation_date = None
		self.expiration_date = None

class Analytics:
	def __init__(self, url, access_date, location):
		self.url = url
		self.access_date = access_date
		self.location = location

	@classmethod
	def create(cls, url, access_date, location):
		return cls(url, access_date, location)

	def get_details(self):
		return {
			'url': self.url.get_details(),
			'access_date': self.access_date.strftime('%Y-%m-%d %H:%M:%S'),
			'location': self.location
		}
