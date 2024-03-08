from typing import Dict, Optional
from datetime import datetime

mock_db = {}
mock_click_db = {}
mock_user_db = {}


class URL:
	def __init__(self, original_url: str, shortened_url: str, user: Optional[str] = None, expiration: Optional[datetime] = None):
		self.original_url = original_url
		self.shortened_url = shortened_url
		self.user = user
		self.expiration = expiration


class Click:
	def __init__(self, url: str, timestamp: datetime, location: str):
		self.url = url
		self.timestamp = timestamp
		self.location = location


class User:
	def __init__(self, username: str, password: str):
		self.username = username
		self.password = password
