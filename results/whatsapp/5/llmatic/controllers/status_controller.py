from models.status import Status
from models.user import User

class StatusController:
	def __init__(self):
		self.statuses = []

	def post_status(self, user: User, content: str, visibility_settings: dict):
		status = Status(id='status_id', user=user, content=content, visibility_settings=visibility_settings)
		self.statuses.append(status)

	def view_status(self, user: User):
		visible_statuses = [status for status in self.statuses if user not in status.visibility_settings['blocked']]
		return visible_statuses
