class Contact:
	def __init__(self, name):
		self.name = name
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


class Contacts:
	def __init__(self):
		self.contacts = {}

	def add_contact(self, name):
		self.contacts[name] = Contact(name)

	def get_contact(self, name):
		return self.contacts.get(name, None)

	def block_contact(self, name):
		contact = self.get_contact(name)
		if contact:
			contact.block()

	def unblock_contact(self, name):
		contact = self.get_contact(name)
		if contact:
			contact.unblock()

	def add_contact_to_group(self, name, group):
		contact = self.get_contact(name)
		if contact:
			contact.add_to_group(group)

	def remove_contact_from_group(self, name, group):
		contact = self.get_contact(name)
		if contact:
			contact.remove_from_group(group)
