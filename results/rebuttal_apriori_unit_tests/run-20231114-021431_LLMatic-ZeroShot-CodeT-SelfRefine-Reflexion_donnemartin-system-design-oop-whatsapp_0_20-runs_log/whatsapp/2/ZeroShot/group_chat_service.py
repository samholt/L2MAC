class GroupChatService:
	def __init__(self):
		self.groups = {}
		self.group_id_counter = 0

	def create_group(self, user_id, group_name, group_picture):
		self.group_id_counter += 1
		self.groups[self.group_id_counter] = {'name': group_name, 'picture': group_picture, 'admin': user_id, 'participants': [user_id], 'admin_permissions': {user_id: ['Add members', 'Remove members', 'Edit group info']}}
		return self.group_id_counter

	def add_participant(self, group_id, participant_id):
		if group_id not in self.groups or participant_id in self.groups[group_id]['participants']:
			return False
		self.groups[group_id]['participants'].append(participant_id)
		return True

	def remove_participant(self, group_id, participant_id):
		if group_id not in self.groups or participant_id not in self.groups[group_id]['participants']:
			return False
		self.groups[group_id]['participants'].remove(participant_id)
		return True

	def assign_admin(self, group_id, user_id):
		if group_id not in self.groups or user_id not in self.groups[group_id]['participants']:
			return False
		self.groups[group_id]['admin_permissions'][user_id] = ['Add members', 'Remove members', 'Edit group info']
		return True

	def change_admin_permissions(self, group_id, user_id, new_permissions):
		if group_id not in self.groups or user_id not in self.groups[group_id]['admin_permissions']:
			return False
		self.groups[group_id]['admin_permissions'][user_id] = new_permissions
		return True
