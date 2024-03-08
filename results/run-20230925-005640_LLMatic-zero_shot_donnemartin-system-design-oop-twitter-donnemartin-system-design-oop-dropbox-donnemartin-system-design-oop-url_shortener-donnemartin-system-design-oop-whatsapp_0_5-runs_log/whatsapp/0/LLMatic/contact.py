class Contact:
	def __init__(self, user, contact):
		self.user = user
		self.contact = contact
		self.blocked = False

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False
