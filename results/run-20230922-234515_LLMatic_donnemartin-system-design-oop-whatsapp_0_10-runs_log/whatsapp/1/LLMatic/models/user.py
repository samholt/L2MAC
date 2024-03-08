from dataclasses import dataclass
from typing import Dict

@dataclass
class User:
	id: int
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: Dict[str, bool]
