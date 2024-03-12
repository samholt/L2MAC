from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image: str = None
	id: str = str(uuid.uuid4())
	created_at: str = str(datetime.now())

	def to_dict(self):
		return self.__dict__
