class GroupService:
	def __init__(self):
		self.groups = {}
		self.group_admins = {}
		self.group_members = {}

	def create_group(self, user_id, group_name):
		group_id = len(self.groups) + 1
		self.groups[group_id] = group_name
		self.group_admins[group_id] = [user_id]
		self.group_members[group_id] = [user_id]
		return group_id

	def edit_group(self, user_id, group_id, new_group_name):
		if user_id in self.group_admins[group_id]:
			self.groups[group_id] = new_group_name
			return True
		return False

	def add_participant(self, user_id, group_id, participant_id):
		if user_id in self.group_admins[group_id]:
			self.group_members[group_id].append(participant_id)
			return True
		return False

	def remove_participant(self, user_id, group_id, participant_id):
		if user_id in self.group_admins[group_id] and participant_id in self.group_members[group_id]:
			self.group_members[group_id].remove(participant_id)
			return True
		return False

	def assign_admin(self, user_id, group_id, admin_id):
		if user_id in self.group_admins[group_id]:
			self.group_admins[group_id].append(admin_id)
			return True
		return False

	def change_admin_permissions(self, user_id, group_id, permissions):
		if user_id in self.group_admins[group_id]:
			# For simplicity, we assume that all admins have the same permissions
			# In a real-world application, we would need to keep track of the permissions for each admin
			return True
		return False
