class Post:
	def __init__(self):
		self.posts_db = {}

	def create_post(self, user, content, image):
		from datetime import datetime
		timestamp = datetime.now()
		if user not in self.posts_db:
			self.posts_db[user] = []
		self.posts_db[user].append({'content': content, 'image': image, 'timestamp': timestamp, 'likes': [], 'retweets': [], 'replies': []})
		return 'Post created successfully'

	def delete_post(self, user, post_id):
		if user in self.posts_db and len(self.posts_db[user]) > post_id:
			del self.posts_db[user][post_id]
			return 'Post deleted successfully'
		else:
			return 'Post not found'

	def like_post(self, user, post_id):
		if user in self.posts_db and len(self.posts_db[user]) > post_id:
			self.posts_db[user][post_id]['likes'].append(user)
			return 'Post liked successfully'
		else:
			return 'Post not found'

	def retweet_post(self, user, post_id):
		if user in self.posts_db and len(self.posts_db[user]) > post_id:
			self.posts_db[user][post_id]['retweets'].append(user)
			return 'Post retweeted successfully'
		else:
			return 'Post not found'

	def reply_to_post(self, user, post_id, content):
		if user in self.posts_db and len(self.posts_db[user]) > post_id:
			self.posts_db[user][post_id]['replies'].append({'user': user, 'content': content})
			return 'Reply added successfully'
		else:
			return 'Post not found'
