class Profile:
	def __init__(self, user):
		self.user = user
		self.followers = []
		self.reading_list = []

	def follow(self, user):
		if user not in self.followers:
			self.followers.append(user)

	def add_to_reading_list(self, book):
		if book not in self.reading_list:
			self.reading_list.append(book)
