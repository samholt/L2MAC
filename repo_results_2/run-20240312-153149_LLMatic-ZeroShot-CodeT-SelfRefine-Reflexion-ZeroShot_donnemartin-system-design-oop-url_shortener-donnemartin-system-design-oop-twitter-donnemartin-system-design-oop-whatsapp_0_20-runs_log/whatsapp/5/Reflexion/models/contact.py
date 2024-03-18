from dataclasses import dataclass

@dataclass
class Contact:
	id: str
	user_id: str
	contact_id: str
	blocked: bool = False
