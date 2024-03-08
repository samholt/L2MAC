class GroupService:
	def __init__(self):
		self.groups = {}

	def create_group(self, group_id, group_name):
		if group_id not in self.groups:
			self.groups[group_id] = {'name': group_name, 'participants': [], 'admins': []}
		return self.groups[group_id]

	def add_participant(self, group_id, user_id):
		if group_id in self.groups:
			self.groups[group_id]['participants'].append(user_id)
		return self.groups[group_id]

	def remove_participant(self, group_id, user_id):
		if group_id in self.groups and user_id in self.groups[group_id]['participants']:
			self.groups[group_id]['participants'].remove(user_id)
		return self.groups[group_id]

	def set_admin(self, group_id, user_id):
		if group_id in self.groups and user_id in self.groups[group_id]['participants']:
			self.groups[group_id]['admins'].append(user_id)
		return self.groups[group_id]
