class Post:
	def __init__(self, user, content, hashtags):
		self.user = user
		self.content = content
		self.hashtags = hashtags
		self.likes = 0
		self.retweets = 0
		self.replies = []

	def like(self, user):
		self.likes += 1
		self.user.create_notification('like', self)

	def retweet(self, user):
		self.retweets += 1
		self.user.create_notification('retweet', self)

	def reply(self, user, content):
		self.replies.append(content)
		self.user.create_notification('reply', self)


class PostingContentManagement:
	def __init__(self):
		self.posts = []

	def create_post(self, user, content, hashtags):
		self.posts.append(Post(user, content, hashtags))
