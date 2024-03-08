class Forum:
	def __init__(self, id, book_club, threads=[]):
		self.id = id
		self.book_club = book_club
		self.threads = threads

	def create_forum(self, id, book_club):
		self.id = id
		self.book_club = book_club
		self.threads = []

	def add_thread(self, thread):
		self.threads.append(thread)

	def update_forum(self, id=None, book_club=None):
		if id is not None:
			self.id = id
		if book_club is not None:
			self.book_club = book_club
