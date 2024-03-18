from dataclasses import dataclass, field
from .user import User

@dataclass
class Post:
	user: User
	content: str
	likes: dict = field(default_factory=dict)
	retweets: dict = field(default_factory=dict)
	replies: list = field(default_factory=list)
	images: list = field(default_factory=list)
