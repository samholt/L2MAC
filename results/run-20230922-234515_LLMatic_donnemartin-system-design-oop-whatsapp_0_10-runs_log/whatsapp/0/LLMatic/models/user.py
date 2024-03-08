from dataclasses import dataclass

@dataclass
class User:
	id: int
	email: str
	password: str
	profile_picture: str
	status_message: str
	last_seen_status: str
	privacy_settings: dict
