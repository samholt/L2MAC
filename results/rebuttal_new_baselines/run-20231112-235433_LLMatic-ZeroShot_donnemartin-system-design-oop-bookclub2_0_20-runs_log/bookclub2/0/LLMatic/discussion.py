class Discussion:
	def __init__(self, book_club, topic):
		self.book_club = book_club
		self.topic = topic
		self.comments = []
		self.votes = {}

	def create_discussion(self, book_club, topic):
		self.book_club = book_club
		self.topic = topic

	def add_comment(self, user, comment):
		self.comments.append({'user': user, 'comment': comment})

	def vote_for_next_book(self, user, book):
		if book not in self.votes:
			self.votes[book] = []
		self.votes[book].append(user)
