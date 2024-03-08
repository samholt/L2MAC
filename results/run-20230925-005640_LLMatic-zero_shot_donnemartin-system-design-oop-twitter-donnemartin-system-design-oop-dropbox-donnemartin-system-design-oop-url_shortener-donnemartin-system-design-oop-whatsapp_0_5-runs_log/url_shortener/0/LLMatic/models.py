from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime

@dataclass
class User:
	username: str
	password: str

	def to_dict(self):
		return {'username': self.username, 'password': self.password}

@dataclass
class URL:
	original_url: str
	short_url: str
	user: str
	clicks: int
	click_data: List[Dict]
	expiration_date: datetime

	def to_dict(self):
		return {
			'original_url': self.original_url,
			'short_url': self.short_url,
			'user': self.user,
			'clicks': self.clicks,
			'click_data': self.click_data,
			'expiration_date': self.expiration_date
		}
