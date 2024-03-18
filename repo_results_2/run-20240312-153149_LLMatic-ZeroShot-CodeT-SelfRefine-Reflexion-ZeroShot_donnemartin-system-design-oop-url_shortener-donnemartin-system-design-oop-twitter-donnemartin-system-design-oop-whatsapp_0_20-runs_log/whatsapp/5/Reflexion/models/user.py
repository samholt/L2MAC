from dataclasses import dataclass

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None
