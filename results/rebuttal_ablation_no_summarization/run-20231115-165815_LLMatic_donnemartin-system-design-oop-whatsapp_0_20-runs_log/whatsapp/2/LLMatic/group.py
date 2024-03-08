class Group:
	def __init__(self, name, admin, picture=None):
		self.name = name
		self.admin = admin
		self.picture = picture
		self.members = {admin}
		self.admins = {admin}

	def add_member(self, member):
		self.members.add(member)

	def remove_member(self, member):
		self.members.remove(member)

	def edit_group(self, new_name, new_picture=None):
		self.name = new_name
		if new_picture is not None:
			self.picture = new_picture

	def manage_admin_roles(self, action, member):
		if action == 'add' and member in self.members:
			self.admins.add(member)
		elif action == 'remove' and member in self.admins:
			self.admins.remove(member)

	def manage_group(self, action, member):
		if action == 'add':
			self.add_member(member)
		elif action == 'remove':
			self.remove_member(member)
