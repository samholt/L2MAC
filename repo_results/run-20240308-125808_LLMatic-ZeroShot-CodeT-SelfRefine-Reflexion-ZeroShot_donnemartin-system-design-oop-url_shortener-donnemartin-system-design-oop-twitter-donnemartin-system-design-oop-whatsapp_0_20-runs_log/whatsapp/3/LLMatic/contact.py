class Contact:
	def __init__(self, email):
		self.email = email
		self.blocked = False
		self.groups = []

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False

	def add_to_group(self, group):
		self.groups.append(group)

	def remove_from_group(self, group):
		if group in self.groups:
			self.groups.remove(group)
