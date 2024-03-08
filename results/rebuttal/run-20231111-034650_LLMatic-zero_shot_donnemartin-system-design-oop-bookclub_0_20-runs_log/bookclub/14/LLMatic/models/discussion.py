class Discussion:
	def __init__(self, id, topic, book_club, comments=[]):
		self.id = id
		self.topic = topic
		self.book_club = book_club
		self.comments = comments

	@classmethod
	def create_discussion(cls, id, topic, book_club):
		return cls(id, topic, book_club)

	def add_comment(self, comment):
		self.comments.append(comment)
