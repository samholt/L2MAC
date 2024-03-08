class Thread:
	def __init__(self, id, title):
		self.id = id
		self.title = title
		self.comments = []

	def create_thread(self, id, title):
		return Thread(id, title)

	def add_comment(self, comment):
		self.comments.append(comment)

	def remove_comment(self, comment):
		if comment in self.comments:
			self.comments.remove(comment)

	def get_info(self):
		return {'id': self.id, 'title': self.title, 'comments': self.comments}
