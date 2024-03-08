class Status:
	def __init__(self, user):
		self.user = user
		self.statuses = []
		self.viewers = []

	def post_status(self, image):
		self.statuses.append(image)
		return True

	def add_viewer(self, user):
		self.viewers.append(user)
		return True

	def remove_viewer(self, user):
		self.viewers.remove(user)
		return True

	def get_status(self):
		return self.statuses

	def get_viewers(self):
		return self.viewers
