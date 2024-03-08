class Status:
	def __init__(self):
		self.status_db = {}

	def post_status(self, user_id, status, visibility):
		if user_id not in self.status_db:
			self.status_db[user_id] = []
		self.status_db[user_id].append({'status': status, 'visibility': visibility})

	def view_statuses(self, user_id):
		visible_statuses = []
		for id, statuses in self.status_db.items():
			for status in statuses:
				if status['visibility'] == 'public' or id == user_id:
					visible_statuses.append(status)
		return visible_statuses

	def manage_status_visibility(self, user_id, status_id, visibility):
		for status in self.status_db.get(user_id, []):
			if id(status) == status_id:
				status['visibility'] = visibility
				return True
		return False
