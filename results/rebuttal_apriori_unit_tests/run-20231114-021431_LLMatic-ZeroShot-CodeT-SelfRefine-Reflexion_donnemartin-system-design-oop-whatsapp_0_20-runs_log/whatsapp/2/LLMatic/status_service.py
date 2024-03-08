import time


class StatusService:
	def __init__(self):
		self.statuses = {}

	def post_image_status(self, user_id, image_status, duration):
		if user_id not in self.statuses:
			self.statuses[user_id] = {}
		status_id = len(self.statuses[user_id]) + 1
		self.statuses[user_id][status_id] = {'image_status': image_status, 'expiry_time': time.time() + duration * 3600}
		return True

	def set_status_visibility(self, user_id, visibility_settings):
		if user_id not in self.statuses:
			self.statuses[user_id] = {}
		self.statuses[user_id]['visibility_settings'] = visibility_settings
		return True
