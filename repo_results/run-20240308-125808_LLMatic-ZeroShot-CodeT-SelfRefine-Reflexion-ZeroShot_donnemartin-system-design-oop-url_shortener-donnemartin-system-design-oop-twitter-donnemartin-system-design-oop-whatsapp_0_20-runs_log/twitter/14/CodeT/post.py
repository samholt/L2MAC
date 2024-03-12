from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Post:
	email: str
	content: str
	id: str = str(uuid.uuid4())
	timestamp: str = str(datetime.utcnow())

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'content': self.content,
			'timestamp': self.timestamp
		}
