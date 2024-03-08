from dataclasses import dataclass

@dataclass
class Message:
	sender_id: int
	receiver_id: int
	text: str
	read_status: bool
	encryption_key: str
