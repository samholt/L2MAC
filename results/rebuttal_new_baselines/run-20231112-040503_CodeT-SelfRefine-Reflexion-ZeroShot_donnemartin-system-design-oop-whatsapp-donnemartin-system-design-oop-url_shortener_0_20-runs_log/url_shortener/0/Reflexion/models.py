from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
	id: str
	username: str
	password: str


@dataclass
class URL:
	id: str
	original_url: str
	shortened_url: str
	user_id: str
	expiration: datetime
	clicks: int
	click_data: list


@dataclass
class Click:
	id: str
	url_id: str
	timestamp: datetime
	location: str
