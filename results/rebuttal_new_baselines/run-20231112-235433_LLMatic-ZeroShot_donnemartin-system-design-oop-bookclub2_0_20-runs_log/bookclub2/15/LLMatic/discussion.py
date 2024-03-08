class Discussion:
	def __init__(self):
		self.forums = {}
		self.comments = {}
		self.votes = {}

	def create_forum(self, forum_name):
		if forum_name not in self.forums:
			self.forums[forum_name] = []
			self.comments[forum_name] = []

	def post_comment(self, forum_name, comment):
		if forum_name in self.forums:
			self.comments[forum_name].append(comment)

	def vote_for_book(self, book_name):
		if book_name not in self.votes:
			self.votes[book_name] = 0
		self.votes[book_name] += 1
