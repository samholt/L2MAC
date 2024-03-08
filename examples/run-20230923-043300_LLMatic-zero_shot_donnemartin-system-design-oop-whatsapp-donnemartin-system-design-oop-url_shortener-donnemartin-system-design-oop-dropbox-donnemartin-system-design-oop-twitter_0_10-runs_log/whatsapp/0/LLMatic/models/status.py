from dataclasses import dataclass
import datetime

@dataclass
class Status:
	id: int
	user: str
	image: str
	visibility: str
	timestamp: datetime.datetime
