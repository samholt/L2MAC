class Group:
	def __init__(self, name, admin):
		self.name = name
		self.admin = admin
		self.members = {admin: 'admin'}

	def add_member(self, user):
		if user not in self.members:
			self.members[user] = 'member'
			return True
		return False

	def remove_member(self, user):
		if user in self.members and self.members[user] != 'admin':
			del self.members[user]
			return True
		return False

	def promote_to_admin(self, admin, user):
		if self.members[admin] == 'admin' and user in self.members:
			self.members[user] = 'admin'
			return True
		return False

	def demote_from_admin(self, admin, user):
		if self.members[admin] == 'admin' and user in self.members:
			self.members[user] = 'member'
			return True
		return False

class Groups:
	def __init__(self):
		self.groups = {}

	def create_group(self, name, admin):
		if name not in self.groups:
			self.groups[name] = Group(name, admin)
			return True
		return False

	def get_group(self, name):
		return self.groups.get(name, None)

	def delete_group(self, name):
		if name in self.groups:
			del self.groups[name]
			return True
		return False
