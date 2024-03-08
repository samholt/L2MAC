import datetime

class Post:
	def __init__(self, content, images, user):
		self.content = content
		self.images = images
		self.user = user
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.timestamp = datetime.datetime.now()

	def create_post(self):
		# In a real application, you would save these details in a database
		print(f'Post created by {self.user.username} with content: {self.content}')

	def delete_post(self):
		# In a real application, you would delete the post from the database
		print(f'Post by {self.user.username} deleted')

	def like_post(self):
		self.likes += 1
		print(f'Post by {self.user.username} liked. Total likes: {self.likes}')

	def retweet_post(self):
		self.retweets += 1
		print(f'Post by {self.user.username} retweeted. Total retweets: {self.retweets}')

	def reply_to_post(self, reply):
		self.replies.append(reply)
		print(f'Reply added to the post by {self.user.username}. Total replies: {len(self.replies)}')
