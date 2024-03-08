class StatusService:
	def __init__(self):
		self.status_db = {}

	def post_image_status(self, user_id, image_status, duration):
		if user_id not in self.status_db:
			self.status_db[user_id] = {}
		self.status_db[user_id]['image_status'] = image_status
		self.status_db[user_id]['duration'] = duration
		return True

	def set_status_visibility(self, user_id, visibility):
		if user_id not in self.status_db:
			self.status_db[user_id] = {}
		self.status_db[user_id]['visibility'] = visibility
		return True
