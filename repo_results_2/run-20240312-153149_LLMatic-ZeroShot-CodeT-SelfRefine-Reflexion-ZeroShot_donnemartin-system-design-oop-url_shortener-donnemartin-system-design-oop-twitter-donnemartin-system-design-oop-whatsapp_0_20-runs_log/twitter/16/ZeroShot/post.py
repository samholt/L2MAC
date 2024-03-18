from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = field(default='')
	id: str = field(default_factory=lambda: str(uuid4()))
	created_at: datetime = field(default_factory=datetime.now)

	def to_dict(self):
		return {key: value for key, value in self.__dict__.items()}
