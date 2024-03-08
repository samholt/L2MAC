from dataclasses import dataclass, field
from typing import List

@dataclass
class Post:
	author: str
	content: str
	images: List[str]
	likes: int = field(default=0)
	retweets: int = field(default=0)
	replies: List[str] = field(default_factory=list)

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, reply):
		self.replies.append(reply)

	def delete(self):
		self.content = ''
		self.images = []
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@staticmethod
	def search(posts, keyword):
		return [post for post in posts if keyword in post.content]
