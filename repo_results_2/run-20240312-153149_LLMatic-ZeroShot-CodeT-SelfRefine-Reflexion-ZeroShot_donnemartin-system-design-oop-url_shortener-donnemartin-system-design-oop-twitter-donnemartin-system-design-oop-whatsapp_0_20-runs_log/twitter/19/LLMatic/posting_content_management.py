class Post:
	def __init__(self, user, content, image=None):
		self.user = user
		self.content = content[:280]
		self.image = image
		self.likes = 0
		self.retweets = 0
		self.comments = []

	def like(self):
		self.likes += 1

	def retweet(self):
		self.retweets += 1

	def reply(self, comment):
		self.comments.append(comment)

	def delete(self):
		print(f'Post by {self.user} deleted.')

	def search(self, keyword):
		return keyword in self.content

	def filter(self, keyword):
		return keyword in self.content


class Comment:
	def __init__(self, user, content, reply_to):
		self.user = user
		self.content = content
		self.reply_to = reply_to
		self.replies = []

	def reply(self, comment):
		self.replies.append(comment)
