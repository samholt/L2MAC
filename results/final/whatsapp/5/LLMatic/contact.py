class Contact:
	def __init__(self, user):
		self.user = user
		self.blocked_contacts = []
		self.groups = []

	def block_contact(self, user):
		self.blocked_contacts.append(user)

	def unblock_contact(self, user):
		self.blocked_contacts.remove(user)

	def create_group(self, group):
		self.groups.append(group)

	def edit_group(self, group, new_group):
		index = self.groups.index(group)
		self.groups[index] = new_group

	def delete_group(self, group):
		self.groups.remove(group)
