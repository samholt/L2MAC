import datetime


class URL:
	def __init__(self, original_url, short_url, user, expiration_date=None):
		self.original_url = original_url
		self.short_url = short_url
		self.user = user
		self.created_at = datetime.datetime.now()
		self.expiration_date = expiration_date
		self.clicks = []


class Click:
	def __init__(self, url, timestamp, location):
		self.url = url
		self.timestamp = timestamp
		self.location = location


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = []


class URLDatabase:
	def __init__(self):
		self.db = {}

	def add_url(self, url):
		self.db[url.short_url] = url

	def get_url(self, short_url):
		return self.db.get(short_url)

	def get_analytics(self, short_url):
		url = self.get_url(short_url)
		if url:
			return {
				'original_url': url.original_url,
				'short_url': url.short_url,
				'user': url.user,
				'created_at': url.created_at,
				'expiration_date': url.expiration_date,
				'clicks': url.clicks
			}
		return None

	def record_click(self, short_url, timestamp, location):
		url = self.get_url(short_url)
		if url:
			click = Click(url, timestamp, location)
			url.clicks.append(click)
