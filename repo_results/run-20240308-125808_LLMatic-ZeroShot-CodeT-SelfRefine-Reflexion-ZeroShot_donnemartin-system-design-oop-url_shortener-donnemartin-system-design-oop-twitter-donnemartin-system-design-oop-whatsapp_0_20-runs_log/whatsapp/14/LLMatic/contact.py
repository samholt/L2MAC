class Contact:
	def __init__(self, name):
		self.name = name
		self.blocked = False

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False


class Group:
	def __init__(self, group_name):
		self.group_name = group_name
		self.members = []

	def add_member(self, contact):
		if not contact.blocked:
			self.members.append(contact)

	def remove_member(self, contact):
		if contact in self.members:
			self.members.remove(contact)

	def edit_group_name(self, new_name):
		self.group_name = new_name
