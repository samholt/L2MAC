class BookSelection:
	def __init__(self):
		self.books = {}
		self.votes = {}

	def suggest_book(self, book_id, user_id):
		if book_id not in self.books:
			self.books[book_id] = {'suggested_by': user_id, 'votes': 0}
		return self.books

	def vote_for_book(self, book_id, user_id):
		if book_id in self.books:
			self.books[book_id]['votes'] += 1
			if book_id not in self.votes:
				self.votes[book_id] = [user_id]
			else:
				self.votes[book_id].append(user_id)
		return self.books, self.votes

	def get_book_data(self, book_id):
		# Mocking a database call
		book_database = {
			'1': {'title': 'Book 1', 'author': 'Author 1'},
			'2': {'title': 'Book 2', 'author': 'Author 2'},
			'3': {'title': 'Book 3', 'author': 'Author 3'}
		}
		return book_database.get(book_id, 'Book not found')

