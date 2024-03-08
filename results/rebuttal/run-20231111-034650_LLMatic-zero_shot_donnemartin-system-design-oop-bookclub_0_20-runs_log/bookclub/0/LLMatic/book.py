class Book:
	def __init__(self, title, author, reviews=[]):
		self.title = title
		self.author = author
		self.reviews = reviews

	def suggest_book(self, user, book):
		# This method should integrate with a book database
		# For now, we'll just print the suggestion
		print(f'{user} suggests {book}')

	def vote_for_book(self, user, book):
		# This method should integrate with a book database
		# For now, we'll just print the vote
		print(f'{user} votes for {book}')
