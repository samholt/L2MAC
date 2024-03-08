from datetime import datetime, timedelta


class Status:
	def __init__(self, user, content, visibility, expiry):
		self.user = user
		self.content = content
		self.visibility = visibility
		self.expiry = expiry

	def post(self):
		# Add status to user's status list
		self.user.status.append(self)

	def view(self, viewer):
		# Return status if viewer is in visibility list and current time is before expiry
		if viewer in self.visibility and datetime.now() < self.expiry:
			return self.content

	def delete(self):
		# Remove status from user's status list
		self.user.status.remove(self)
