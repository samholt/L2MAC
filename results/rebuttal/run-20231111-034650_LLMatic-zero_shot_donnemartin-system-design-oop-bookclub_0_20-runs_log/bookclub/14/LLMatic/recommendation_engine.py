class RecommendationEngine:
	def __init__(self, users, books):
		self.users = users
		self.books = books

	def recommend_books(self, user):
		read_books = set(user.books)
		unread_books = [book for book in self.books if book.id not in read_books]

		# Sort the unread books by the number of book clubs they are in (popularity)
		unread_books.sort(key=lambda book: len(book.book_clubs), reverse=True)

		return unread_books[:5]  # Return the top 5 recommendations
