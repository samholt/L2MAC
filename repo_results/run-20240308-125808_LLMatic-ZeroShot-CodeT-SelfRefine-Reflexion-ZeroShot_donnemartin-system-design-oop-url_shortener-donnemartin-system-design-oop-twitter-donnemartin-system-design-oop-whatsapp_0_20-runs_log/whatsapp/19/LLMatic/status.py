class Status:
	def __init__(self, user, image, visibility_time, viewers):
		self.user = user
		self.image = image
		self.visibility_time = visibility_time
		self.viewers = viewers

	def post_image_status(self, image, visibility_time):
		self.image = image
		self.visibility_time = visibility_time

	def manage_viewers(self, viewers):
		self.viewers = viewers
