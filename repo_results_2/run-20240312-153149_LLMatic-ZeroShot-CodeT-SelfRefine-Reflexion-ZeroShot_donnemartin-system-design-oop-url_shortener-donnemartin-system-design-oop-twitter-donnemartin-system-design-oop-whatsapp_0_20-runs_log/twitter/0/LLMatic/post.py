from datetime import datetime
from collections import Counter
import re


class Post:
	posts = {}

	def __init__(self, id, title, content, user_id):
		self.id = id
		self.title = title
		self.content = content
		self.user_id = user_id
		self.timestamp = datetime.now()
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@classmethod
	def create_post(cls, title, content, user_id):
		new_post = Post(len(cls.posts) + 1, title, content, user_id)
		cls.posts[new_post.id] = new_post
		return new_post

	@classmethod
	def delete_post(cls, post_id):
		if post_id in cls.posts:
			del cls.posts[post_id]
			return True
		return False

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_post(self, reply):
		self.replies.append(reply)

	@classmethod
	def search_posts(cls, keyword):
		return [post for post in cls.posts.values() if keyword in post.content]

	@classmethod
	def trending_topics(cls):
		hashtags = [re.findall(r'#\w+', post.content) for post in cls.posts.values()]
		hashtags = [hashtag for sublist in hashtags for hashtag in sublist]
		return Counter(hashtags).most_common(5)
