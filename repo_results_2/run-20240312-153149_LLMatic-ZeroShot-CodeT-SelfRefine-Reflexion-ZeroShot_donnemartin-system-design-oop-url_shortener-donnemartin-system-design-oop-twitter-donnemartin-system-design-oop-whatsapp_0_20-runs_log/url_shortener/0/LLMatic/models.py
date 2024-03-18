from dataclasses import dataclass
from datetime import datetime


@dataclass
class URL:
	original_url: str
	short_url: str
	user: str
	expirationDate: datetime


@dataclass
class Click:
	timestamp: datetime
	location: str
	short_url: str


@dataclass
class User:
	username: str
	password: str
	urls: list
	isAdmin: bool = False
