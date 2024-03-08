class Post:
	def __init__(self, text, images, user):
		self.text = text
		self.images = images
		self.user = user
		self.likes = 0
		self.retweets = 0
		self.replies = []

	@staticmethod
	def create_post(text, images, user):
		return Post(text, images, user)

	@staticmethod
	def delete_post(post):
		post.text = None
		post.images = None
		post.user = None

	def like_post(self):
		self.likes += 1

	def retweet_post(self):
		self.retweets += 1

	def reply_to_post(self, reply):
		self.replies.append(reply)

	def display_replies(self):
		for reply in self.replies:
			print(reply)

	@staticmethod
	def search_posts(posts, keyword):
		return [post for post in posts if keyword in post.text]

	@staticmethod
	def filter_posts(posts, filter):
		return [post for post in posts if filter in post.text]
