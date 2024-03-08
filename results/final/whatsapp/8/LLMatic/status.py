from datetime import datetime, timedelta
from user import User


class Status:
	def __init__(self, user: User, image: str, visibility: str = 'public', expiry_time: datetime = datetime.now() + timedelta(hours=24)):
		self.user = user
		self.image = image
		self.visibility = visibility
		self.expiry_time = expiry_time
		self.status_db = {}

	def post(self):
		self.status_db[self.user.email] = {'image': self.image, 'visibility': self.visibility, 'expiry_time': self.expiry_time}

	def view(self):
		return self.status_db.get(self.user.email, 'No status found')

	def set_visibility(self, visibility: str):
		if self.user.email in self.status_db:
			self.status_db[self.user.email]['visibility'] = visibility
		else:
			print('No status found for this user')

