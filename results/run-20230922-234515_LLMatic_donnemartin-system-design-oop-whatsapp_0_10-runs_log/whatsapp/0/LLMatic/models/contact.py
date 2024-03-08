from dataclasses import dataclass

@dataclass
class Contact:
	user_id: int
	contact_id: int
	blocked: bool
