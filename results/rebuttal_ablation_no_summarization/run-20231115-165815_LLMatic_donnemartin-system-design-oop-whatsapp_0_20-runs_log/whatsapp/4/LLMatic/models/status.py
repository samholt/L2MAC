class Status:
	def __init__(self, id, user, image, visibility, time_limit):
		self.id = id
		self.user = user
		self.image = image
		self.visibility = visibility
		self.time_limit = time_limit

	def to_dict(self):
		return {
			'id': self.id,
			'user': self.user,
			'image': self.image,
			'visibility': self.visibility,
			'time_limit': self.time_limit
		}

	def __repr__(self):
		return str(self.to_dict())
