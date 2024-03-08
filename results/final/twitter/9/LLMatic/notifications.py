from models import Notification, users_db, notifications_db


def get_notifications(user_id):
	return sorted([notification for notification in notifications_db.values() if notification.user_id == user_id], key=lambda notification: notification.timestamp, reverse=True)

