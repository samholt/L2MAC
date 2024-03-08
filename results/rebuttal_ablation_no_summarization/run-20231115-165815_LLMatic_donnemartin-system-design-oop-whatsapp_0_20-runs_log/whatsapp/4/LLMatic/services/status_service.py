class StatusService:
	def __init__(self):
		self.status_db = {}

	def post_status(self, id, user, image, visibility, time_limit):
		from models.status import Status
		new_status = Status(id, user, image, visibility, time_limit)
		self.status_db[id] = new_status
		return new_status

	def set_visibility(self, id, visibility):
		status = self.status_db.get(id)
		if status:
			status.visibility = visibility
		return status

	def set_time_limit(self, id, time_limit):
		status = self.status_db.get(id)
		if status:
			status.time_limit = time_limit
		return status
