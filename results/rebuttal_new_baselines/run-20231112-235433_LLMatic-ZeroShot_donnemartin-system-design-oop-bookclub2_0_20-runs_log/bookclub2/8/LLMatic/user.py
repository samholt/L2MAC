class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.book_clubs = []

	def authenticate(self, username, password):
		return self.username == username and self.password == password

	def join_book_club(self, book_club):
		self.book_clubs.append(book_club)
		return self.book_clubs
