class Thread:
	def __init__(self, id, title, author):
		self.id = id
		self.title = title
		self.author = author
		self.comments = []

	def add_comment(self, comment):
		self.comments.append(comment)

	def update_thread(self, title=None, author=None):
		if title is not None:
			self.title = title
		if author is not None:
			self.author = author
