class Contact:
	def __init__(self, email):
		self.email = email
		self.blocked = False

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False
