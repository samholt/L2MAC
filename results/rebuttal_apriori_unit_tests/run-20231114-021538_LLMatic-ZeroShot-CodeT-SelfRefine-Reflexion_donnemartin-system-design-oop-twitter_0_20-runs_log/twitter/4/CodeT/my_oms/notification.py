from dataclasses import dataclass

@dataclass
class Notification:
	id: int
	user_id: int
	content: str
