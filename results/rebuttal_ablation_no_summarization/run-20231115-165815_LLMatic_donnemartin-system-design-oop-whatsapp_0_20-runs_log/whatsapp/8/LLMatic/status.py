class Status:
	def __init__(self):
		self.status = None
		self.visibility = 'public'
		self.image_file = None

	def post_status(self, image_file, visibility):
		self.image_file = image_file
		self.visibility = visibility
		self.status = 'Posted'

	def view_status(self):
		if self.status == 'Posted':
			return {'status': self.status, 'image_file': self.image_file, 'visibility': self.visibility}
		else:
			return 'No status posted yet'

	def control_visibility(self, visibility):
		self.visibility = visibility
