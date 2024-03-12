from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Post:
	id: str
	user_email: str
	content: str
	image_url: str = field(default=None)
	created_at: datetime = field(default_factory=datetime.now)

	def to_dict(self):
		return {**self.__dict__, 'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S')}
