import datetime


class Status:
	def __init__(self, user_id, image, visibility_duration=24, visible_to='everyone'):
		self.user_id = user_id
		self.image = image
		self.posted_at = datetime.datetime.now()
		self.visibility_duration = visibility_duration
		self.visible_to = visible_to

	def update_visibility_settings(self, visibility_duration, visible_to):
		self.visibility_duration = visibility_duration
		self.visible_to = visible_to

	def is_visible(self):
		return (datetime.datetime.now() - self.posted_at).total_seconds() / 3600 < self.visibility_duration

	def post_status(self):
		if self.is_visible():
			return {'status': 'success', 'message': 'Status posted successfully.'}
		else:
			return {'status': 'failed', 'message': 'Status is no longer visible.'}
