from dataclasses import dataclass, field
from typing import List
from post import Post
from user import User

@dataclass
class TrendingTopic:
	topic_name: str
	related_posts: List[Post] = field(default_factory=list)

	def add_post(self, post: Post):
		if self.topic_name in post.content:
			self.related_posts.append(post)

	def display_trending(self):
		return sorted(self.related_posts, key=lambda post: post.likes + post.retweets, reverse=True)

	@staticmethod
	def recommend_users(users: List[User], interests: List[str], activity: int, mutual_followers: int):
		recommended_users = [user for user in users if any(interest in user.bio for interest in interests) and len(user.posts) >= activity and len(user.followers) >= mutual_followers]
		return recommended_users
