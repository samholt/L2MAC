class User:
	def __init__(self, name, email, password, reading_interests=[], books_read=[], books_to_read=[]):
		self.name = name
		self.email = email
		self.password = password
		self.reading_interests = reading_interests
		self.books_read = books_read
		self.books_to_read = books_to_read
		self.following = []

	def follow(self, user):
		if user not in self.following:
			self.following.append(user)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
