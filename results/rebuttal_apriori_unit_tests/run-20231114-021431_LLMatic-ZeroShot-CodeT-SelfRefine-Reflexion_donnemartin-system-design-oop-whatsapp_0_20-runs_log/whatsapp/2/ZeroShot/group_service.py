class GroupService:
	def __init__(self):
		self.groups = {}
		self.group_id_counter = 0

	def create_group(self, user_id, group_name):
		self.group_id_counter += 1
		self.groups[self.group_id_counter] = {'name': group_name, 'admin': user_id}
		return self.group_id_counter

	def edit_group(self, user_id, group_id, new_group_name):
		if group_id not in self.groups or self.groups[group_id]['admin'] != user_id:
			return False
		self.groups[group_id]['name'] = new_group_name
		return True
