from dataclasses import dataclass

@dataclass
class Message:
	id: int
	sender_id: int
	receiver_id: int
	content: str
