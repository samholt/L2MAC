from datetime import datetime
from database import Database

class Status:
	def __init__(self, user, content, visibility):
		self.user = user
		self.content = content
		self.timestamp = None
		self.visibility = visibility

	def post(self):
		self.timestamp = datetime.now()
		Database.add_status(self)
