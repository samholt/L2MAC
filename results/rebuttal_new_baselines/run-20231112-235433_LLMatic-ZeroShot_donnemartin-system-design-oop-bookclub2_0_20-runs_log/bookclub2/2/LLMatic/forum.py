class Forum:
	def __init__(self, id, title):
		self.id = id
		self.title = title
		self.threads = []

	def create_forum(self, id, title):
		self.id = id
		self.title = title

	def add_thread(self, thread):
		self.threads.append(thread)

	def remove_thread(self, thread):
		if thread in self.threads:
			self.threads.remove(thread)

	def get_info(self):
		return {'id': self.id, 'title': self.title, 'threads': self.threads}
