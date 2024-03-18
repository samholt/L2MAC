from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Post:
	user_email: str
	content: str
	image_url: str = ''
	likes: int = field(default=0, repr=False)
	retweets: int = field(default=0, repr=False)
	replies: int = field(default=0, repr=False)
	id: str = field(default_factory=lambda: str(uuid.uuid4()), repr=False)
	created_at: datetime = field(default_factory=datetime.now, repr=False)

	def to_dict(self):
		return {f.name: getattr(self, f.name) for f in fields(self)}
