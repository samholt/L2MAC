from dataclasses import dataclass

# Mock database
notifications_db = {}

@dataclass
class Notification:
	id: int
	content: str
	recipient: str
	related_post_or_user: str

	@classmethod
	def create_notification(cls, id: int, content: str, recipient: str, related_post_or_user: str):
		if id in notifications_db:
			return 'Notification already exists'
		else:
			notifications_db[id] = cls(id, content, recipient, related_post_or_user)
			return 'Notification created'

	@classmethod
	def delete_notification(cls, id: int):
		if id in notifications_db:
			del notifications_db[id]
			return 'Notification deleted'
		else:
			return 'Notification does not exist'

	@classmethod
	def notify_users(cls, id: int, content: str, recipient: str, related_post_or_user: str):
		cls.create_notification(id, content, recipient, related_post_or_user)
		return 'User notified'
