class Status:
	def __init__(self, user, message, visibility):
		self.user = user
		self.message = message
		self.visibility = visibility

	def set_message(self, message):
		self.message = message
		return 'Status message set successfully'

	def set_visibility(self, visibility):
		self.visibility = visibility
		return 'Visibility set successfully'
