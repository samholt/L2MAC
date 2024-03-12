class Group:
	def __init__(self, name, picture=None):
		self.name = name
		self.picture = picture
		self.contacts = []
		self.admins = []

	def create_group(self, name, picture=None):
		return Group(name, picture)

	def add_contact(self, contact):
		self.contacts.append(contact)

	def remove_contact(self, contact):
		self.contacts.remove(contact)

	def add_admin(self, contact):
		if contact not in self.admins:
			self.admins.append(contact)

	def remove_admin(self, contact):
		if contact in self.admins:
			self.admins.remove(contact)
