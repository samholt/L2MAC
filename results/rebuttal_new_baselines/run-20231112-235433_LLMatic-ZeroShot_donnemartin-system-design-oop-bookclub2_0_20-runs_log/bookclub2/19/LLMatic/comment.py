class Comment:
	def __init__(self, id, content, author, thread):
		self.id = id
		self.content = content
		self.author = author
		self.thread = thread

	def create_comment(self, id, content, author, thread):
		self.id = id
		self.content = content
		self.author = author
		self.thread = thread

	def update_comment(self, content):
		self.content = content
