class Group:
	def __init__(self):
		self.groups = {}

	def create_group(self, group_name, admin, picture=None):
		if group_name in self.groups:
			return 'Group already exists'
		self.groups[group_name] = {'admin': admin, 'members': [admin], 'blocked_members': [], 'picture': picture}
		return 'Group created successfully'

	def add_member(self, group_name, member):
		if group_name not in self.groups:
			return 'Group does not exist'
		if member in self.groups[group_name]['members']:
			return 'Member already in group'
		self.groups[group_name]['members'].append(member)
		return 'Member added successfully'

	def remove_member(self, group_name, member):
		if group_name not in self.groups:
			return 'Group does not exist'
		if member not in self.groups[group_name]['members']:
			return 'Member not in group'
		self.groups[group_name]['members'].remove(member)
		return 'Member removed successfully'

	def block_member(self, group_name, member):
		if group_name not in self.groups:
			return 'Group does not exist'
		if member in self.groups[group_name]['blocked_members']:
			return 'Member already blocked'
		self.groups[group_name]['blocked_members'].append(member)
		return 'Member blocked successfully'

	def unblock_member(self, group_name, member):
		if group_name not in self.groups:
			return 'Group does not exist'
		if member not in self.groups[group_name]['blocked_members']:
			return 'Member not blocked'
		self.groups[group_name]['blocked_members'].remove(member)
		return 'Member unblocked successfully'

	def get_group(self, group_name):
		return self.groups.get(group_name, None)
