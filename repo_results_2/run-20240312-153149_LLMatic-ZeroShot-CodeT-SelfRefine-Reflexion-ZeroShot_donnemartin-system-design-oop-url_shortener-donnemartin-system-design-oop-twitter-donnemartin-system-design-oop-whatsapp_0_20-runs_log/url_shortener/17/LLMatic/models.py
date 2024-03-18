from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime


@dataclass
class URL:
	original_url: str
	short_url: str
	user: str
	clicks: int = 0
	click_details: List[Dict[str, str]] = field(default_factory=list)
	expiration_date: datetime = None


@dataclass
class User:
	username: str
	password: str
	isAdmin: bool = False
	urls: List[URL] = field(default_factory=list)
