class Book:
	def __init__(self):
		self.books = {}

	def suggest_book(self, title, author):
		if title not in self.books:
			self.books[title] = {'author': author, 'votes': 0, 'reviews': []}
			return 'Book suggested successfully'
		else:
			return 'Book already suggested'

	def vote_book(self, title):
		if title in self.books:
			self.books[title]['votes'] += 1
			return 'Vote added successfully'
		else:
			return 'Book not found'

	def add_review(self, title, review):
		if title in self.books:
			self.books[title]['reviews'].append(review)
			return 'Review added successfully'
		else:
			return 'Book not found'
