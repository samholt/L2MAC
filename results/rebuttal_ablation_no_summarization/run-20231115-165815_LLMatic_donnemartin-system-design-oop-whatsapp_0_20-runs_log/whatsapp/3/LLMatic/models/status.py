import uuid
class Status:
	def __init__(self, user, content, visibility, time_limit):
		self.id = str(uuid.uuid4())
		self.user = user
		self.content = content
		self.visibility = visibility
		self.time_limit = time_limit

