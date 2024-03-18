from models.notification import Notification

notifications = {}

def create_notification(user, content):
	notification = Notification(user, content)
	notifications[user.email] = notification
	return notification

def get_notification(user):
	return notifications.get(user.email, None)
