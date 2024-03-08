class StatusService:
	def __init__(self):
		self.statuses = {}

	def post_image_status(self, user_id, image_status, duration):
		self.statuses[user_id] = (image_status, duration)
		return True

	def set_status_visibility(self, user_id, visibility_settings):
		if user_id in self.statuses:
			self.statuses[user_id] = (self.statuses[user_id][0], visibility_settings)
			return True
		return False
