from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	id: str = None
	timestamp: str = None

	def __post_init__(self):
		self.id = self.id or str(uuid.uuid4())
		self.timestamp = self.timestamp or datetime.utcnow().isoformat()

	def to_dict(self):
		return {'id': self.id, 'user_email': self.user_email, 'content': self.content, 'timestamp': self.timestamp}
