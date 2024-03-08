from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
	username: str
	password: str

@dataclass
class URL:
	original_url: str
	shortened_url: str
	user: User
	expiration_date: datetime

@dataclass
class Click:
	url: URL
	click_time: datetime
	location: str

