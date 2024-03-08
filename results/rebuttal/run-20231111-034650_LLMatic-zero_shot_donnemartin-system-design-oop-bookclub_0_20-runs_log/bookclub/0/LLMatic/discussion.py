class Discussion:
	def __init__(self, topic, book_club, comments=[]):
		self.topic = topic
		self.book_club = book_club
		self.comments = comments

	def create_discussion(self, topic, book_club):
		self.topic = topic
		self.book_club = book_club
		self.comments = []

	def add_comment(self, comment):
		self.comments.append(comment)

	def upload_image(self, image):
		self.comments = [{'type': 'image', 'content': image}]

	def upload_link(self, link):
		self.comments = [{'type': 'link', 'content': link}]
