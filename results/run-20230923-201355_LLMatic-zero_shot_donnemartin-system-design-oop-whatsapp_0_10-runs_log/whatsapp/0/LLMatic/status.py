class Status:
	def __init__(self, user, image, visibility, expiry_time):
		self.user = user
		self.image = image
		self.visibility = visibility
		self.expiry_time = expiry_time
		self.status_db = {}

	def post_status(self):
		self.status_db[self.user.email] = {'image': self.image, 'visibility': self.visibility, 'expiry_time': self.expiry_time}
