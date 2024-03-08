from datetime import datetime, timedelta
from user import User
from connectivity import connectivity, restore_connectivity


class Status:
	def __init__(self, user: User, content: str, visibility: str, duration: int):
		self.user = user
		self.content = content
		self.visibility = visibility
		self.expiry = datetime.now() + timedelta(hours=duration)
		self.status_id = f'{user.email}_{datetime.now().strftime("%Y%m%d%H%M%S")}'
		self.queue = []

	def post(self, db: dict):
		if datetime.now() <= self.expiry:
			if connectivity():
				db[self.status_id] = self
			else:
				self.queue.append((self.post, [db]))
				restore_connectivity(self.queue, db)

	def view(self, db: dict):
		if datetime.now() <= self.expiry:
			return db.get(self.status_id, None)
		else:
			db.pop(self.status_id, None)
			return None
