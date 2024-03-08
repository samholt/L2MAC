class Discussion:
	def __init__(self, book_club, book, comments=[]):
		self.book_club = book_club
		self.book = book
		self.comments = comments

	def add_comment(self, comment):
		self.comments.append(comment)

	def get_comments(self):
		return self.comments
