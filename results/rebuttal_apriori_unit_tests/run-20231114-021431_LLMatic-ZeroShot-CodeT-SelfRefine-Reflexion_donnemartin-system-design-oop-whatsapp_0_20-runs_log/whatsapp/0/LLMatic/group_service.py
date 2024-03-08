class GroupService:
	def __init__(self):
		self.groups = {}
		self.group_id = 0

	def create_group(self, user_id, group_name):
		self.group_id += 1
		self.groups[self.group_id] = {'name': group_name, 'admin': user_id, 'participants': [user_id], 'permissions': {user_id: 'all'}}
		return self.group_id

	def edit_group(self, user_id, group_id, new_group_name):
		if user_id == self.groups[group_id]['admin']:
			self.groups[group_id]['name'] = new_group_name
			return True
		return False

	def add_participant(self, group_id, participant_id):
		if participant_id not in self.groups[group_id]['participants']:
			self.groups[group_id]['participants'].append(participant_id)
			return True
		return False

	def remove_participant(self, group_id, participant_id):
		if participant_id in self.groups[group_id]['participants']:
			self.groups[group_id]['participants'].remove(participant_id)
			return True
		return False

	def assign_admin(self, group_id, user_id):
		if user_id in self.groups[group_id]['participants']:
			self.groups[group_id]['admin'] = user_id
			return True
		return False

	def change_admin_permissions(self, group_id, user_id, new_permissions):
		if user_id == self.groups[group_id]['admin']:
			self.groups[group_id]['permissions'][user_id] = new_permissions
			return True
		return False
