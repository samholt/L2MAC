class Notification:
	def __init__(self, notification_type, triggered_by, received_by):
		self.notification_type = notification_type
		self.triggered_by = triggered_by
		self.received_by = received_by

	def get_notification(self):
		return {
			'type': self.notification_type,
			'triggered_by': self.triggered_by.username,
			'received_by': self.received_by.username
		}
