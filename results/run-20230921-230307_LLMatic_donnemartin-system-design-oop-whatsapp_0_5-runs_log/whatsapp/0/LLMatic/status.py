from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Status:
	def __init__(self):
		self.user = None
		self.image = None
		self.visibility = None
		self.time_limit = timedelta(hours=24)
		self.post_time = None

	def post_status(self, user, image, visibility):
		self.user = user
		self.image = image
		self.visibility = visibility
		self.post_time = datetime.now()

	def is_visible(self):
		if datetime.now() - self.post_time > self.time_limit:
			return False
		return True

