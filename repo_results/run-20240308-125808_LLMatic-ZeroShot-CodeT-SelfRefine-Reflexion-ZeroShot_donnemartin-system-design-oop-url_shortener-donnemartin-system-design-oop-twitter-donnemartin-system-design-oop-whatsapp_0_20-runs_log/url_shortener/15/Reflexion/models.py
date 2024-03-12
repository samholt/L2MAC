from dataclasses import dataclass
from typing import List, Dict


@dataclass
class User:
	id: str
	username: str
	password: str
	urls: List[str]


@dataclass
class URL:
	id: str
	original_url: str
	shortened_url: str
	user_id: str
	clicks: List[Dict]
	expiration: str

