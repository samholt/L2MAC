import time

# Mocking a database with an in-memory dictionary
posts_db = {}


class Post:
	def __init__(self, user_id, text, image=None):
		self.user_id = user_id
		self.text = text
		self.image = image
		self.timestamp = None
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def create(self):
		if len(self.text) > 280:
			return 'Error: The post text exceeds the limit of 280 characters.'
		self.timestamp = time.time()
		# Mocking a database with an in-memory dictionary
		posts_db[self.user_id] = {'text': self.text, 'image': self.image, 'timestamp': self.timestamp, 'likes': self.likes, 'retweets': self.retweets, 'replies': self.replies}
		return 'Post created successfully.'

	def delete(self):
		if self.user_id in posts_db:
			del posts_db[self.user_id]
			return 'Post deleted successfully.'
		return 'Error: Post not found.'

	def like(self):
		self.likes += 1
		posts_db[self.user_id]['likes'] = self.likes
		return 'Post liked.'

	def retweet(self):
		self.retweets += 1
		posts_db[self.user_id]['retweets'] = self.retweets
		return 'Post retweeted.'

	def reply(self, user_id, text, image=None):
		reply = Post(user_id, text, image)
		reply.create()
		self.replies.append(reply)
		posts_db[self.user_id]['replies'] = [reply.user_id for reply in self.replies]
		return 'Reply posted.'
