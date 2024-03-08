class Contact:
	def __init__(self, user):
		self.user = user
		self.blocked_contacts = []
		self.groups = []

	def block_contact(self, user):
		if user not in self.blocked_contacts:
			self.blocked_contacts.append(user)

	def unblock_contact(self, user):
		if user in self.blocked_contacts:
			self.blocked_contacts.remove(user)

	def create_group(self, group):
		if group not in self.groups:
			self.groups.append(group)

	def edit_group(self, group, new_group):
		if group in self.groups:
			index = self.groups.index(group)
			self.groups[index] = new_group

	def manage_group(self, group):
		if group in self.groups:
			return group
