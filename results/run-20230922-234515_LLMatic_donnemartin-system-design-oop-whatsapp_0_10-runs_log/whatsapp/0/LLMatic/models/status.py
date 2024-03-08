from dataclasses import dataclass
import datetime

@dataclass
class Status:
	user_id: str
	image: str
	visibility: str
	timestamp: datetime = datetime.datetime.now()
