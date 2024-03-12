class Contact:
	def __init__(self, name, blocked=False, admin=False):
		self.name = name
		self.blocked = blocked
		self.admin = admin

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False

	def make_admin(self):
		self.admin = True

	def remove_admin(self):
		self.admin = False
