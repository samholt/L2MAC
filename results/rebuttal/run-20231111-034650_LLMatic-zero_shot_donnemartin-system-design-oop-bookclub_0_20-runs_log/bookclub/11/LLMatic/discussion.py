class Discussion:
	def __init__(self):
		self.discussions = {}

	def create_discussion(self, topic, book_club):
		if topic in self.discussions:
			return 'Discussion already exists'
		self.discussions[topic] = {'book_club': book_club, 'comments': []}
		return 'Discussion created successfully'

	def post_comment(self, topic, comment):
		if topic not in self.discussions:
			return 'Discussion does not exist'
		self.discussions[topic]['comments'].append(comment)
		return 'Comment posted successfully'
