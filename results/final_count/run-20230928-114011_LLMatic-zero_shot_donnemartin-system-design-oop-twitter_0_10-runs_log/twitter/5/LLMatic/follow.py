from dataclasses import dataclass, field
from typing import List
from post import Post

@dataclass
class Follow:
	follower: str
	followed: str
	followed_posts: List[Post] = field(default_factory=list)

	def follow(self, user):
		self.followed = user

	def unfollow(self, user):
		if self.followed == user:
			self.followed = None

	def display_timeline(self):
		return self.followed_posts
