from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = ''
	likes: int = 0
	retweets: int = 0
	replies: int = 0
	id: str = str(uuid.uuid4())
	created_at: datetime = datetime.now()

	def to_dict(self):
		return {key: value for key, value in self.__dict__.items()}
