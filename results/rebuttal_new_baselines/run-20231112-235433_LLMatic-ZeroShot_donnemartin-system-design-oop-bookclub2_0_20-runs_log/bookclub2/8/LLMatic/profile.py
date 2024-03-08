class Profile:
	def __init__(self, user):
		self.user = user
		self.followers = []
		self.books_read = []

	def follow(self, user):
		if user not in self.followers:
			self.followers.append(user)

	def add_book(self, book):
		if book not in self.books_read:
			self.books_read.append(book)
