class Recommendation:
	def __init__(self):
		self.recommendations = {}

	def generate_recommendation(self, user):
		# This is a placeholder. In a real-world application, this method would analyze the user's reading history and generate recommendations accordingly.
		# For this task, we'll simply return a static list of books.
		self.recommendations[user] = ['Book 1', 'Book 2', 'Book 3']
		return self.recommendations[user]

	def popular_books(self):
		# This is a placeholder. In a real-world application, this method would analyze the reading habits of all users and highlight the most popular books.
		# For this task, we'll simply return a static list of books.
		return ['Book 1', 'Book 2', 'Book 3']
