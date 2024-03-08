class StatusService:
	def __init__(self):
		self.statuses = {}

	def post_image_status(self, user_id, image_status, duration):
		self.statuses[user_id] = {'image': image_status, 'duration': duration}
		return True

	def set_status_visibility(self, user_id, visibility_settings):
		if user_id not in self.statuses:
			return False
		self.statuses[user_id]['visibility'] = visibility_settings
		return True
