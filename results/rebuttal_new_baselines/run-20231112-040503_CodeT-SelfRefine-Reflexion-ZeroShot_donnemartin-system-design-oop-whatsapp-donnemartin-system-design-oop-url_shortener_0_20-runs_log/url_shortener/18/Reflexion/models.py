from dataclasses import dataclass

@dataclass
class User:
	id: str
	username: str
	password: str

@dataclass
class UrlData:
	id: str
	original_url: str
	shortened_url: str
	user_id: str
	clicks: int
	expiration_date: str
	geographical_location: str
