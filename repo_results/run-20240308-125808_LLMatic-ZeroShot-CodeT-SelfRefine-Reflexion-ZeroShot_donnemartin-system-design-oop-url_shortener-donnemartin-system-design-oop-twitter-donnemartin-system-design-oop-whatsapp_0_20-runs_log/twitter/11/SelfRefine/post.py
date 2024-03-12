from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image: str = field(default=None)
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	created_at: datetime = field(default_factory=datetime.now)

	def to_dict(self):
		created_at = self.created_at
		if isinstance(created_at, datetime):
			created_at = created_at.strftime('%a, %d %b %Y %H:%M:%S GMT')
		return {**self.__dict__, 'created_at': created_at}
