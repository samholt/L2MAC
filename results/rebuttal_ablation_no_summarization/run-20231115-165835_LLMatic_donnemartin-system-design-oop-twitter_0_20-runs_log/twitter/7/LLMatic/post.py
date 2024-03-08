from dataclasses import dataclass
from typing import Dict, Optional
import auth

# Mock database
posts_db: Dict[int, 'Post'] = {}
comments_db: Dict[int, 'Comment'] = {}

@dataclass
class Post:
	user: str
	text: Optional[str] = None
	images: Optional[str] = None
	likes: int = 0
	retweets: int = 0

@dataclass
class Comment:
	user: str
	post: Post
	text: str


def create_post(user: str, text: Optional[str], images: Optional[str]) -> Post:
	"""Create a new post."""
	post = Post(user, text, images)
	post_id = len(posts_db) + 1
	posts_db[post_id] = post
	return post


def delete_post(post_id: int) -> bool:
	"""Delete a post."""
	if post_id in posts_db:
		del posts_db[post_id]
		return True
	return False


def create_comment(user: str, post: Post, text: str) -> Comment:
	"""Create a new comment."""
	comment = Comment(user, post, text)
	comment_id = len(comments_db) + 1
	comments_db[comment_id] = comment
	return comment


def like_post(post_id: int) -> bool:
	"""Like a post."""
	if post_id in posts_db:
		posts_db[post_id].likes += 1
		return True
	return False


def retweet_post(post_id: int) -> bool:
	"""Retweet a post."""
	if post_id in posts_db:
		posts_db[post_id].retweets += 1
		return True
	return False


def search(keyword: str) -> Dict[str, list]:
	"""Search for posts and users that match the keyword."""
	matching_posts = [post for post in posts_db.values() if keyword in post.text]
	matching_users = [user for user in auth.users_db.values() if keyword in user.username]
	return {'posts': matching_posts, 'users': matching_users}


def filter(content: str) -> list:
	"""Filter posts by hashtag, user mention, or trending topic."""
	filtered_posts = [post for post in posts_db.values() if content in post.text]
	return filtered_posts


def get_trending_topics() -> Dict[str, int]:
	"""Get trending topics based on the volume and velocity of mentions."""
	topics = {}
	for post in posts_db.values():
		words = post.text.split()
		for word in words:
			if word.startswith('#'):
				topics[word] = topics.get(word, 0) + 1
	return topics


def get_user_recommendations(username: str) -> list:
	"""Recommend users to follow based on interests, activity, and mutual followers."""
	# This is a simple recommendation system that recommends the users who have the most followers.
	# A more sophisticated system could take into account shared interests, activity, and mutual followers.
	user_followers = {user.username: len(user.followers) for user in auth.users_db.values() if user.username != username}
	recommended_users = sorted(user_followers, key=user_followers.get, reverse=True)[:5]
	return recommended_users
