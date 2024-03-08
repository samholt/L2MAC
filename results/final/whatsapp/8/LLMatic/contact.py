class Contact:
	def __init__(self, user):
		self.user = user
		self.blocked_contacts = []
		self.groups = []

	def block_contact(self, contact):
		self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		if contact in self.blocked_contacts:
			self.blocked_contacts.remove(contact)

	def create_group(self, group_name):
		self.groups.append({'name': group_name, 'members': []})

	def edit_group(self, group_name, new_group_name):
		for group in self.groups:
			if group['name'] == group_name:
				group['name'] = new_group_name
				break

	def manage_group(self, group_name, action, member=None):
		for group in self.groups:
			if group['name'] == group_name:
				if action == 'add' and member is not None:
					group['members'].append(member)
				elif action == 'remove' and member is not None:
					if member in group['members']:
						group['members'].remove(member)
				break
