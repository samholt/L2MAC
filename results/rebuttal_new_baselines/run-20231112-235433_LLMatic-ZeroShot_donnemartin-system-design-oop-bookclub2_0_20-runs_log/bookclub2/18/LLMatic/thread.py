class Thread:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.comments = []

	def add_comment(self, comment):
		self.comments.append(comment)
