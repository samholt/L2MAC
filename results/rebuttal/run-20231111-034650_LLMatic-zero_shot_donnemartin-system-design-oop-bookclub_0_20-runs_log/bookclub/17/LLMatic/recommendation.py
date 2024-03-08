class Recommendation:
	def __init__(self, database):
		self.database = database

	def get_user_books(self, user_id):
		user = self.database.get(self.database.users, user_id)
		return user['books'] if user and 'books' in user else []

	def get_popular_books(self):
		books = self.database.books.values()
		return sorted(books, key=lambda x: x.votes, reverse=True)

	def recommend(self, user_id):
		user_books = self.get_user_books(user_id)
		popular_books = self.get_popular_books()
		recommendations = [book for book in popular_books if book.id not in user_books]
		return recommendations[:5]
