from dataclasses import dataclass

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	bio: str = ''
	website: str = ''
	location: str = ''
	is_private: bool = False
	followers: list = None
	following: list = None
	likes: list = None
	retweets: list = None
	mentions: list = None
	messages: list = None
	notifications: list = None
	
	def __post_init__(self):
		self.followers = []
		self.following = []
		self.likes = []
		self.retweets = []
		self.mentions = []
		self.messages = []
		self.notifications = []
