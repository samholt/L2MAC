from datetime import datetime


class Status:
	def __init__(self, user_id, status_content=None):
		self.user_id = user_id
		self.status_content = status_content
		self.created_at = datetime.now()

	def post_status(self, status_content):
		self.status_content = status_content
		self.created_at = datetime.now()

	def view_status(self):
		return {
			'user_id': self.user_id,
			'status_content': self.status_content,
			'created_at': self.created_at
		}
