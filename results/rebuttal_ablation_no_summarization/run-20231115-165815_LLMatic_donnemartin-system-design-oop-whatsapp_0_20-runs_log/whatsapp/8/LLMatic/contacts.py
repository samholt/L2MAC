class Contact:
	def __init__(self, name):
		self.name = name
		self.blocked = False
		self.groups = []

	def block_contact(self):
		self.blocked = True

	def unblock_contact(self):
		self.blocked = False

	def create_group(self, group_name, contacts):
		self.groups.append({"group_name": group_name, "contacts": contacts})

	def edit_group(self, group_name, contacts):
		for group in self.groups:
			if group['group_name'] == group_name:
				group['contacts'] = contacts

	def manage_groups(self):
		return self.groups
