class RecommendationEngine:
	def __init__(self, db):
		self.db = db

	def recommend_books_based_on_history(self, user):
		# For simplicity, we'll just recommend the first book in the user's to-read list
		# In a real-world application, this would use a more sophisticated algorithm
		if user.books_to_read:
			return user.books_to_read[0]
		else:
			return None

	def highlight_popular_books(self):
		# For simplicity, we'll just return the book with the most reviews
		# In a real-world application, this would use a more sophisticated algorithm
		most_reviews = 0
		most_reviewed_book = None
		for book in self.db.books.values():
			if len(book.reviews) > most_reviews:
				most_reviews = len(book.reviews)
				most_reviewed_book = book
		return most_reviewed_book
