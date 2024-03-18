import datetime

class Status:
	def __init__(self, user, content, visibility, expiration_time):
		self.user = user
		self.content = content
		self.visibility = visibility
		self.expiration_time = expiration_time
		self.posted_time = datetime.datetime.now()

	def is_expired(self):
		return datetime.datetime.now() > self.posted_time + datetime.timedelta(seconds=self.expiration_time)
