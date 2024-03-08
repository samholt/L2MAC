from dataclasses import dataclass
import datetime

db = {}

@dataclass
class User:
	id: str
	name: str
	email: str
	urls: list

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'email': self.email, 'urls': [url.to_dict() for url in self.urls]}

@dataclass
class URL:
	original_url: str
	shortened_url: str
	user_id: str
	expiration_date: datetime.datetime

	def to_dict(self):
		return {'original_url': self.original_url, 'shortened_url': self.shortened_url, 'user_id': self.user_id, 'expiration_date': self.expiration_date.isoformat()}
