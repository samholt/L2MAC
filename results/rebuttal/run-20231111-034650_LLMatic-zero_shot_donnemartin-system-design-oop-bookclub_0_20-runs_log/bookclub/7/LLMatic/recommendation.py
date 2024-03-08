class Recommendation:
	def __init__(self):
		self.recommendations = {}
		self.popular_books = {}

	def recommend_book(self, user_id, book_id):
		if user_id not in self.recommendations:
			self.recommendations[user_id] = []
		self.recommendations[user_id].append(book_id)

	def get_recommendations(self, user_id):
		return self.recommendations.get(user_id, [])

	def highlight_popular_book(self, book_id):
		if book_id not in self.popular_books:
			self.popular_books[book_id] = 0
		self.popular_books[book_id] += 1

	def get_popular_books(self):
		return sorted(self.popular_books.items(), key=lambda x: x[1], reverse=True)
