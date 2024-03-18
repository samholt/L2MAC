from dataclasses import dataclass
from typing import Dict, List
import time


@dataclass
class User:
	username: str
	password: str
	urls: Dict[str, str] = {}

	def add_url(self, original_url: str, shortened_url: str):
		self.urls[shortened_url] = original_url

	def delete_url(self, shortened_url: str):
		if shortened_url in self.urls:
			del self.urls[shortened_url]


@dataclass
class Admin(User):
	def delete_user(self, user: User):
		# In a real application, this would delete the user from the database
		pass


@dataclass
class URL:
	original_url: str
	shortened_url: str
	user: User
	clicks: List[Dict[str, str]] = []
	expiration_date: int = None

	def add_click(self, click_data: Dict[str, str]):
		self.clicks.append(click_data)

	def is_expired(self):
		if self.expiration_date is None:
			return False
		return time.time() > self.expiration_date
