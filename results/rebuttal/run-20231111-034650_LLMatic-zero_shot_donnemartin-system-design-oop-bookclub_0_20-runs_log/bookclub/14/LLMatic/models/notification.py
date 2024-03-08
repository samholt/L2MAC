class Notification:
	def __init__(self, id, user, message, read_status=False):
		self.id = id
		self.user = user
		self.message = message
		self.read_status = read_status

	def create_notification(self, user, message):
		self.user = user
		self.message = message
		self.read_status = False

	def update_read_status(self):
		self.read_status = True
