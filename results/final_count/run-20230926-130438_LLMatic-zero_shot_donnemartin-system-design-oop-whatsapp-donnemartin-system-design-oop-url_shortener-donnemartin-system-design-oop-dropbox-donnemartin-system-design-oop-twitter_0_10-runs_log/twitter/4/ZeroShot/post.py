from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = ''
	id: str = str(uuid.uuid4())
	created_at: datetime = datetime.now()

	def to_dict(self):
		return {
			'id': self.id,
			'user_email': self.user_email,
			'content': self.content,
			'image_url': self.image_url,
			'created_at': self.created_at.isoformat()
		}
