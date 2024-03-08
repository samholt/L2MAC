from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = ''
	id: str = uuid4().hex

	def to_dict(self):
		return {
			'id': self.id,
			'user_email': self.user_email,
			'content': self.content,
			'image_url': self.image_url
		}
