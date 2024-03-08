class BookClub:
	def __init__(self, name, description, is_private):
		self.name = name
		self.description = description
		self.is_private = is_private
		self.members = []
		self.books = []

	def add_member(self, user):
		self.members.append(user)

	def add_book(self, book):
		self.books.append(book)
