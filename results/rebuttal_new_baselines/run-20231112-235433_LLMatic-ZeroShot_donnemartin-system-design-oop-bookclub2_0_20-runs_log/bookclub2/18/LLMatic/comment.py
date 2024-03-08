class Comment:
	def __init__(self, content, author, thread):
		self.content = content
		self.author = author
		self.thread = thread
		self.upvotes = 0
		self.downvotes = 0

	def upvote(self):
		self.upvotes += 1

	def downvote(self):
		self.downvotes += 1
