class Book:
	def __init__(self, id, title, author, description):
		self.id = id
		self.title = title
		self.author = author
		self.description = description
		self.votes = 0

	def suggest(self, title, author, description):
		self.title = title
		self.author = author
		self.description = description

	def get_data(self):
		return {'id': self.id, 'title': self.title, 'author': self.author, 'description': self.description, 'votes': self.votes}

	def update_data(self, title, author, description):
		self.title = title
		self.author = author
		self.description = description

	def delete(self):
		self.id = None
		self.title = None
		self.author = None
		self.description = None
		self.votes = 0
