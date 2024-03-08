class Status:
	def __init__(self, user, image, visibility):
		self.user = user
		self.image = image
		self.visibility = visibility

	def post(self):
		# Add the status to the user's list of statuses
		self.user.statuses.append(self)

	def view(self, viewer):
		# Return the statuses of the user's contacts based on the visibility settings
		return [status for contact in viewer.contacts for status in contact.statuses if status.visibility == 'public']

	def manage(self):
		# Allow the user to delete a status
		self.user.statuses.remove(self)
