class Notification:
	def __init__(self, user, type, post=None):
		self.user = user
		self.type = type
		self.post = post
		self.viewed = False

	def view_notification(self):
		self.viewed = True
		return self

