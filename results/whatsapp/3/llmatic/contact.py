class Contact:
	def __init__(self):
		self.blocked_contacts = []
		self.groups = []

	def block_contact(self, contact):
		self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		self.blocked_contacts.remove(contact)

	def create_group(self, group):
		self.groups.append(group)

	def edit_group(self, group, new_group):
		index = self.groups.index(group)
		self.groups[index] = new_group

	def manage_groups(self, group):
		self.groups.remove(group)
