from dataclasses import dataclass
from models.user import User

@dataclass
class Tweet:
	content: str
	poster: User
	privacy: str
	original_tweet: 'Tweet' = None
