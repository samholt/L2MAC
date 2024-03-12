import time


class Status:
	def __init__(self, user, image, visibility='public', duration=24):
		self.user = user
		self.image = image
		self.visibility = visibility
		self.post_time = time.time()
		self.duration = duration
		self.expiry_time = self.post_time + (self.duration * 60 * 60)

	def change_visibility(self, visibility):
		self.visibility = visibility

	def is_expired(self):
		current_time = time.time()
		return current_time > self.expiry_time


def remove_expired_statuses(status_db):
	expired_statuses = [status_id for status_id, status in status_db.items() if status.is_expired()]
	for status_id in expired_statuses:
		del status_db[status_id]
