from datetime import datetime


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = []


class URL:
	def __init__(self, original_url, shortened_url, user=None, creation_date=None, expiration_date=None):
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user = user
		self.creation_date = creation_date or datetime.utcnow()
		self.expiration_date = expiration_date
		self.click_events = []


class ClickEvent:
	def __init__(self, date_time, location):
		self.date_time = date_time
		self.location = location
