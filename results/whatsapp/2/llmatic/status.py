from user import User


class Status:
	def __init__(self, user: User, image, message, visibility='everyone'):
		self.user = user
		self.image = image
		self.message = message
		self.visibility = visibility

	def change_visibility(self, visibility):
		self.visibility = visibility
