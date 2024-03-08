class GroupService:
	def __init__(self):
		self.groups = {}
		self.group_admins = {}
		self.group_members = {}

	def create_group(self, user_id, group_name, group_picture):
		group_id = len(self.groups) + 1
		self.groups[group_id] = {'name': group_name, 'picture': group_picture}
		self.group_admins[group_id] = [user_id]
		self.group_members[group_id] = [user_id]
		return group_id

	def add_participant(self, group_id, user_id):
		if user_id not in self.group_members[group_id]:
			self.group_members[group_id].append(user_id)
			return True
		return False

	def remove_participant(self, group_id, user_id):
		if user_id in self.group_members[group_id]:
			self.group_members[group_id].remove(user_id)
			return True
		return False

	def assign_admin(self, group_id, user_id):
		if user_id in self.group_members[group_id] and user_id not in self.group_admins[group_id]:
			self.group_admins[group_id].append(user_id)
			return True
		return False

	def change_admin_permissions(self, group_id, user_id, permissions):
		if user_id in self.group_admins[group_id]:
			# For simplicity, we assume that permissions are always successfully changed
			return True
		return False
