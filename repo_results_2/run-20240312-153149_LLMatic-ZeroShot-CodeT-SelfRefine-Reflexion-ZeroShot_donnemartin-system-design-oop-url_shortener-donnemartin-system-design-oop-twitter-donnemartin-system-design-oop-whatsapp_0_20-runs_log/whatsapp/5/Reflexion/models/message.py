from dataclasses import dataclass

@dataclass
class Message:
	id: str
	sender_id: str
	receiver_id: str
	content: str
	read: bool = False
	encrypted: bool = False
