class Book:
	def __init__(self, id, title, author, book_clubs=[]):
		self.id = id
		self.title = title
		self.author = author
		self.book_clubs = book_clubs

	@classmethod
	def add_book(cls, id, title, author):
		return cls(id, title, author)

	def get_info(self):
		return {'id': self.id, 'title': self.title, 'author': self.author, 'book_clubs': self.book_clubs}
