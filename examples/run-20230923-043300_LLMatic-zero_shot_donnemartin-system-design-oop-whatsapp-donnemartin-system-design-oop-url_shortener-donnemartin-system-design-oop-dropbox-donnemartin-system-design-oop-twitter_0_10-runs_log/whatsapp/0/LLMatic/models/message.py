from dataclasses import dataclass
from datetime import datetime

@dataclass
class Message:
	id: int
	sender: str
	receiver: str
	content: str
	timestamp: datetime
	read_receipt: bool
