from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class URL:
	original_url: str
	shortened_url: str
	user: str
	creation_date: datetime
	expiration_date: datetime

@dataclass
class Click:
	url: str
	click_date: datetime
	location: str

@dataclass
class User:
	username: str
	password: str
	urls: List[URL]
