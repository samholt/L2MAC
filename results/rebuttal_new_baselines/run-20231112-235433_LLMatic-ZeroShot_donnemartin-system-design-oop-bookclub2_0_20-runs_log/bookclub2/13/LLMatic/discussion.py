class Discussion:
	def __init__(self, topic):
		self.topic = topic
		self.comments = []
		self.votes = 0

	def add_comment(self, comment):
		self.comments.append(comment)

	def upvote(self):
		self.votes += 1

	def downvote(self):
		self.votes -= 1
