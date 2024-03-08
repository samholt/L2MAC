from dataclasses import dataclass
from typing import List
from user import User, users_db, add_notification

# Mock database
posts_db = {}

@dataclass
class Comment:
	user: User
	content: str

@dataclass
class Post:
	id: int
	user: User
	content: str
	images: List[str]
	likes: int = 0
	retweets: int = 0
	comments: List[Comment] = None


def create_post(user: str, content: str, images: List[str]) -> str:
	if user in users_db:
		# Generate post id
		post_id = len(posts_db) + 1
		# Create new post
		post = Post(post_id, users_db[user], content, images)
		# Store post in database
		posts_db[post_id] = post
		return 'Post created successfully'
	else:
		return 'User not found'


def delete_post(user: str, post_id: int) -> str:
	if post_id in posts_db and posts_db[post_id].user.username == user:
		# Delete post from database
		del posts_db[post_id]
		return 'Post deleted successfully'
	else:
		return 'Post not found or user not authorized to delete this post'


def like_post(user: str, post_id: int) -> str:
	if post_id in posts_db:
		post = posts_db[post_id]
		post.likes += 1
		posts_db[post_id] = post
		add_notification(post.user.username, f'{user} liked your post')
		return 'Post liked'
	else:
		return 'Post not found'


def retweet_post(user: str, post_id: int) -> str:
	if post_id in posts_db:
		post = posts_db[post_id]
		post.retweets += 1
		posts_db[post_id] = post
		add_notification(post.user.username, f'{user} retweeted your post')
		return 'Post retweeted'
	else:
		return 'Post not found'


def comment_on_post(user: str, post_id: int, comment_content: str) -> str:
	if post_id in posts_db:
		post = posts_db[post_id]
		comment = Comment(users_db[user], comment_content)
		if post.comments is None:
			post.comments = []
		post.comments.append(comment)
		posts_db[post_id] = post
		add_notification(post.user.username, f'{user} commented on your post')
		return 'Comment added'
	else:
		return 'Post not found'


def search_posts(keyword: str) -> list:
	# Search for posts that match the keyword
	matching_posts = [post for post in posts_db.values() if keyword in post.content]
	return matching_posts


def filter_posts(filter_type: str, value: str) -> list:
	# Filter posts based on filter type and value
	if filter_type == 'hashtag':
		filtered_posts = [post for post in posts_db.values() if value in post.content.split() and value.startswith('#')]
	elif filter_type == 'user_mention':
		filtered_posts = [post for post in posts_db.values() if value in post.content.split() and value.startswith('@')]
		for post in filtered_posts:
			add_notification(value[1:], f'You were mentioned in a post')
	elif filter_type == 'trending_topic':
		filtered_posts = [post for post in posts_db.values() if value in post.content]
	else:
		filtered_posts = []
	return filtered_posts


def get_timeline(username: str) -> list:
	if username in users_db:
		user = users_db[username]
		# Get posts from users that the user is following
		timeline_posts = [post for post in posts_db.values() if post.user.username in user.following]
		return timeline_posts
	else:
		return 'User not found'

