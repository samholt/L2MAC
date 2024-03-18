from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Post:
	user_email: str
	content: str
	image: str = field(default=None)
	id: str = field(default_factory=lambda: str(uuid4()))

	def to_dict(self):
		return {f.name: getattr(self, f.name) for f in fields(self)}
