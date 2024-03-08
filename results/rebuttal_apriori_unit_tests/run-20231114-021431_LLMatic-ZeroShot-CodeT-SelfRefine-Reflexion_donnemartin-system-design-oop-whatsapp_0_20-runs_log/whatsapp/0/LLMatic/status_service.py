class StatusService:
	def __init__(self):
		self.statuses = {}
		self.visibility_settings = {}

	def post_image_status(self, user_id, image_status, duration):
		self.statuses[user_id] = {'image_status': image_status, 'duration': duration}
		return True

	def set_status_visibility(self, user_id, visibility_settings):
		self.visibility_settings[user_id] = visibility_settings
		return True
