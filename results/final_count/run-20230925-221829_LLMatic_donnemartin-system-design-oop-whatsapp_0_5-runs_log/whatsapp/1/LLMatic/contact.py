class Contact:
	def __init__(self):
		self.blocked_contacts = []
		self.groups = {}

	def block_contact(self, user):
		if user not in self.blocked_contacts:
			self.blocked_contacts.append(user)

	def unblock_contact(self, user):
		if user in self.blocked_contacts:
			self.blocked_contacts.remove(user)

	def create_group(self, group_name):
		if group_name not in self.groups:
			self.groups[group_name] = []

	def add_user_to_group(self, group_name, user):
		if group_name in self.groups and user not in self.groups[group_name]:
			self.groups[group_name].append(user)

	def remove_user_from_group(self, group_name, user):
		if group_name in self.groups and user in self.groups[group_name]:
			self.groups[group_name].remove(user)
