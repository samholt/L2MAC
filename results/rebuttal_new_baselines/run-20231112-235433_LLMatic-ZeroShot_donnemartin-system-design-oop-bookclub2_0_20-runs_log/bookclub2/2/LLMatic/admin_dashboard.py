class AdminDashboard:
	def __init__(self, id):
		self.id = id
		self.users = []
		self.book_clubs = []
		self.books = []

	def create_dashboard(self, id):
		self.id = id

	def add_user(self, user):
		self.users.append(user)

	def remove_user(self, user):
		self.users.remove(user)

	def add_book_club(self, book_club):
		self.book_clubs.append(book_club)

	def remove_book_club(self, book_club):
		self.book_clubs.remove(book_club)

	def add_book(self, book):
		self.books.append(book)

	def remove_book(self, book):
		self.books.remove(book)

	def get_info(self):
		return {'id': self.id, 'users': self.users, 'book_clubs': self.book_clubs, 'books': self.books}
