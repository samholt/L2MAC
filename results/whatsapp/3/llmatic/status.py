from datetime import datetime, timedelta


class Status:
	def __init__(self, user, content, visibility):
		self.user = user
		self.content = content
		self.visibility = visibility
		self.post_time = datetime.now()

	def post_status(self, content):
		self.content = content
		self.post_time = datetime.now()

	def set_visibility(self, visibility):
		self.visibility = visibility

	def is_visible(self, viewer):
		if self.visibility == 'public' or viewer.email in self.visibility:
			return True
		return False

	def is_expired(self):
		return datetime.now() - self.post_time > timedelta(hours=24)
