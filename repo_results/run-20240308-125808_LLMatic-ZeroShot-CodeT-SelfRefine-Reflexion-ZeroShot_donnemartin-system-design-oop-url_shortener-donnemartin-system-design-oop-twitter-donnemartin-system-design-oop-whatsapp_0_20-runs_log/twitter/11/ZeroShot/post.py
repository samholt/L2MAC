from dataclasses import dataclass
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = ''
	id: str = str(uuid.uuid4())

	def to_dict(self):
		return self.__dict__
