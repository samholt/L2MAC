class Notification:
	def __init__(self, database):
		self.database = database
		self.notifications = database.notifications

	def create_notification(self, id, data):
		self.database.insert(self.notifications, id, data)

	def get_notification(self, id):
		return self.database.get(self.notifications, id)

	def update_notification(self, id, data):
		if self.get_notification(id):
			self.database.insert(self.notifications, id, data)

	def delete_notification(self, id):
		self.database.delete(self.notifications, id)
