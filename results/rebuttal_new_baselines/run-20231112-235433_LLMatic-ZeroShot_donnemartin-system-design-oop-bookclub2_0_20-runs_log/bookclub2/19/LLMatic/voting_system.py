class VotingSystem:
	def __init__(self, id, book_club, book_options=[]):
		self.id = id
		self.book_club = book_club
		self.book_options = book_options

	def create_voting_system(self, id, book_club):
		self.id = id
		self.book_club = book_club
		self.book_options = []

	def add_book_option(self, book):
		self.book_options.append(book)

	def update_voting_system(self, id=None, book_club=None, book_options=None):
		if id is not None:
			self.id = id
		if book_club is not None:
			self.book_club = book_club
		if book_options is not None:
			self.book_options = book_options
