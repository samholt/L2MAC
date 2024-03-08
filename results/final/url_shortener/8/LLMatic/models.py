from dataclasses import dataclass
from typing import List


@dataclass
class User:
	id: int
	username: str
	password: str
	urls: List['URL']


@dataclass
class URL:
	id: int
	original_url: str
	shortened_url: str
	user_id: int
	clicks: List['Click']
	expiration_date: str


@dataclass
class Click:
	id: int
	url_id: int
	click_time: str
	click_location: str
