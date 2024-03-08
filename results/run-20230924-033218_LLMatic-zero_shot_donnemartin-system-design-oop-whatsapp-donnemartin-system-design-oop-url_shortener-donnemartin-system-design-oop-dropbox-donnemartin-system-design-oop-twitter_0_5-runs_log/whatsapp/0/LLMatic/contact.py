class Contact:
	def __init__(self, name, email, profile_picture, status_message, last_seen, blocked):
		self.name = name
		self.email = email
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.last_seen = last_seen
		self.blocked = blocked

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False

	def view_profile(self):
		return {'name': self.name, 'email': self.email, 'profile_picture': self.profile_picture, 'status_message': self.status_message, 'last_seen': self.last_seen}

	def view_status(self):
		return self.status_message

	def send_message(self, message):
		if not self.blocked:
			return f'Message sent to {self.name}: {message}'
		else:
			return 'Contact is blocked, message not sent.'
