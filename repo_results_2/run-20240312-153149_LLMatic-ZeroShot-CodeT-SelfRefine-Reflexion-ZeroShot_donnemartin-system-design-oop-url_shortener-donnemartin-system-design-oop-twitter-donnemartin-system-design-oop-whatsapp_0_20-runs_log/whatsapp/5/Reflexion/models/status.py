from dataclasses import dataclass

@dataclass
class Status:
	id: str
	user_id: str
	content: str
	visible_to: list = None
