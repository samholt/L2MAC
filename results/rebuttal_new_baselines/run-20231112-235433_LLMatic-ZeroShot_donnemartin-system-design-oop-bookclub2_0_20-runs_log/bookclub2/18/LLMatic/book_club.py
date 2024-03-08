class BookClub:
	def __init__(self, name, privacy_setting):
		self.name = name
		self.privacy_setting = privacy_setting
		self.members = []
		self.books = []

	def add_member(self, user):
		self.members.append(user)

	def add_book(self, book):
		self.books.append(book)
