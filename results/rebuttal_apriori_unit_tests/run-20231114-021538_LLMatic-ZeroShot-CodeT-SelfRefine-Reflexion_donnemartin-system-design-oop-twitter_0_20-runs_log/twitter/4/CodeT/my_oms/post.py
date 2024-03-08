from dataclasses import dataclass

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image: str = None
	likes: list = None
	retweets: list = None
	replies: list = None
	
	def __post_init__(self):
		self.likes = []
		self.retweets = []
		self.replies = []
