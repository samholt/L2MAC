class Contact:
	def __init__(self, email):
		self.email = email
		self.blocked_contacts = set()
		self.groups = {}

	def block_contact(self, contact_email):
		self.blocked_contacts.add(contact_email)

	def unblock_contact(self, contact_email):
		self.blocked_contacts.discard(contact_email)

	def add_to_group(self, group_name, contact_email):
		if group_name not in self.groups:
			self.groups[group_name] = set()
		self.groups[group_name].add(contact_email)

	def remove_from_group(self, group_name, contact_email):
		if group_name in self.groups:
			self.groups[group_name].discard(contact_email)
