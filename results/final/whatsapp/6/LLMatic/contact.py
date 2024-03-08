from user import User

class Contact:
	def __init__(self, user):
		self.user = user
		self.blocked_contacts = []
		self.groups = []

	def block_contact(self, user):
		if user not in self.blocked_contacts:
			self.blocked_contacts.append(user)
			return 'Contact blocked successfully'
		return 'Contact already blocked'

	def unblock_contact(self, user):
		if user in self.blocked_contacts:
			self.blocked_contacts.remove(user)
			return 'Contact unblocked successfully'
		return 'Contact not found in blocked list'

	def create_group(self, group):
		if group not in self.groups:
			self.groups.append(group)
			return 'Group created successfully'
		return 'Group already exists'

	def edit_group(self, group, new_group):
		if group in self.groups:
			index = self.groups.index(group)
			self.groups[index] = new_group
			return 'Group edited successfully'
		return 'Group not found'

	def manage_group(self, group):
		if group in self.groups:
			return 'Group managed'
		return 'Group not found'
