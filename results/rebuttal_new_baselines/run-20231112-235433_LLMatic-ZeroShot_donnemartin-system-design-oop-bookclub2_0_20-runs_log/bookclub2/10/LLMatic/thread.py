class Thread:
	def __init__(self, id, title, creator):
		self.id = id
		self.title = title
		self.creator = creator
		self.comments = []

	def add_comment(self, comment):
		self.comments.append(comment)
