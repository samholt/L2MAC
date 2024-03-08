class Notification:
	def __init__(self, type, content):
		self.type = type
		self.content = content

mock_db = {}


def send_notification(notification):
	mock_db[notification.type] = notification.content
	return 'Notification sent'

def get_notifications(type):
	return mock_db.get(type, 'No notifications of this type')

def set_reminder(type, content):
	mock_db[type] = content
	return 'Reminder set'
