from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = field(default='')
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	created_at: datetime = field(default_factory=datetime.now)

	def to_dict(self):
		return {'id': self.id, 'user_email': self.user_email, 'content': self.content, 'image_url': self.image_url, 'created_at': self.created_at.isoformat()}
