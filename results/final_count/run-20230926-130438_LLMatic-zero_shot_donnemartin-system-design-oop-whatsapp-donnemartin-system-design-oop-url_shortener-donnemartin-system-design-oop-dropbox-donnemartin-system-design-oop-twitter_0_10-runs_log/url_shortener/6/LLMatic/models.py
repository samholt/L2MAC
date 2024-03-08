from datetime import datetime
from typing import List


class User:
	def __init__(self, username: str, password: str):
		self.username = username
		self.password = password
		self.urls = []


class ClickEvent:
	def __init__(self, click_time: datetime, location: str):
		self.click_time = click_time
		self.location = location


class URL:
	def __init__(self, original_url: str, shortened_url: str, user: User, creation_date: datetime, expiration_date: datetime):
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user = user
		self.creation_date = creation_date
		self.expiration_date = expiration_date
		self.click_events = []
