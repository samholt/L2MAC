class Timeline:
	def __init__(self, user):
		self.user = user

	def display(self):
		# In a real-world application, this method would fetch posts from the database
		# Here we just return a success message
		return 'Displaying posts from followed users'
