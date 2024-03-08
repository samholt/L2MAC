class Group:
	def __init__(self):
		self.groups = {}

	def create_group(self, user_id, group_name, member_ids):
		if user_id not in self.groups:
			self.groups[user_id] = {}
		self.groups[user_id][group_name] = member_ids
		return 'Group created successfully'

	def edit_group(self, user_id, old_group_name, new_group_name, new_member_ids):
		if user_id in self.groups and old_group_name in self.groups[user_id]:
			self.groups[user_id][new_group_name] = self.groups[user_id].pop(old_group_name)
			self.groups[user_id][new_group_name] = new_member_ids
			return 'Group edited successfully'
		return 'Group not found'

	def manage_groups(self, user_id):
		return self.groups.get(user_id, 'No groups found')

	def add_participant(self, user_id, group_name, participant_id):
		if user_id in self.groups and group_name in self.groups[user_id] and participant_id not in self.groups[user_id][group_name]:
			self.groups[user_id][group_name].append(participant_id)
			return 'Participant added successfully'
		return 'Group not found or participant already in group'

	def remove_participant(self, user_id, group_name, participant_id):
		if user_id in self.groups and group_name in self.groups[user_id] and participant_id in self.groups[user_id][group_name]:
			self.groups[user_id][group_name].remove(participant_id)
			return 'Participant removed successfully'
		return 'Group not found or participant not in group'

	def manage_admin_roles(self, user_id, group_name, role):
		if user_id in self.groups and group_name in self.groups[user_id]:
			self.groups[user_id][group_name]['admin_role'] = role
			return 'Admin role updated successfully'
		return 'Group not found or user not authorized'

