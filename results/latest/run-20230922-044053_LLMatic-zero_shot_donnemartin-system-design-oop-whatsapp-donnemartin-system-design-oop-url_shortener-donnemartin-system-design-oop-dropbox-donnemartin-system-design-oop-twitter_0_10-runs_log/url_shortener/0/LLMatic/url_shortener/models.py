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
	created_at: datetime
	expires_at: datetime


@dataclass
class Click:
	url: URL
	clicked_at: datetime
	location: str
