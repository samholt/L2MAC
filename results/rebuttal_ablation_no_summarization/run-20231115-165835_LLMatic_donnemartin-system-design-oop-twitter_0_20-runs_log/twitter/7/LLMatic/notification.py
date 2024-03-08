from dataclasses import dataclass
from typing import Dict

# Mock database
notifications_db: Dict[int, 'Notification'] = {}

@dataclass
class Notification:
	user: str
	text: str


def create_notification(user: str, text: str) -> Notification:
	"""Create a new notification."""
	notification = Notification(user, text)
	notification_id = len(notifications_db) + 1
	notifications_db[notification_id] = notification
	return notification
