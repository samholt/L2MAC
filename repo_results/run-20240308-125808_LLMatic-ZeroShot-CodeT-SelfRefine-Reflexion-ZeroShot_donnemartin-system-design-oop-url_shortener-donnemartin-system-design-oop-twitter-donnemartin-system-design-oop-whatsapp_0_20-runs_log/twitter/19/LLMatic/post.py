from datetime import datetime


class Post:
	def __init__(self, user, content, image=None):
		self.author = user
		self.content = content
		self.image = image
		self.timestamp = datetime.now()
		self.post_db = {}
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def create(self):
		if len(self.content) > 280:
			return 'Post content exceeds 280 characters'
		self.post_db[self.timestamp] = {'user': self.author, 'content': self.content, 'image': self.image, 'likes': self.likes, 'retweets': self.retweets, 'replies': self.replies}
		return 'Post created successfully'

	def delete(self):
		if self.timestamp in self.post_db:
			del self.post_db[self.timestamp]
			return 'Post deleted successfully'
		return 'Post not found'

	def like(self):
		self.likes += 1
		self.post_db[self.timestamp]['likes'] = self.likes
		return 'Post liked'

	def retweet(self):
		self.retweets += 1
		self.post_db[self.timestamp]['retweets'] = self.retweets
		return 'Post retweeted'

	def reply(self, user, content):
		reply = Post(user, content)
		reply.create()
		self.replies.append(reply)
		self.post_db[self.timestamp]['replies'] = self.replies
		return 'Reply posted'

	def publish(self, posts_db):
		if self.create() == 'Post created successfully':
			posts_db[self.timestamp] = self
			return 'Post published successfully'
		return 'Failed to publish post'
