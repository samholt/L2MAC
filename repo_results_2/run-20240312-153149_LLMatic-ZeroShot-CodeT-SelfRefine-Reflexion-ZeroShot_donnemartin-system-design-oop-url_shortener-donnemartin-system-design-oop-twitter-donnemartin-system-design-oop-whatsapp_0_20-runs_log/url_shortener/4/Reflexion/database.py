from dataclasses import dataclass
from typing import Dict, List


@dataclass
class URL:
	original_url: str
	short_url: str
	clicks: int
	user_id: str
	expiration_date: str


@dataclass
class User:
	user_id: str
	urls: List[URL]


# Mock database
users: Dict[str, User] = {}
urls: Dict[str, URL] = {}
