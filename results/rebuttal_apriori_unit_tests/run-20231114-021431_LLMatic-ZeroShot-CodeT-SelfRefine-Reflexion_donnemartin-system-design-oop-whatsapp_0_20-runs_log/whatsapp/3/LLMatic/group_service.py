class GroupService:
	def __init__(self):
		self.groups = {}
		self.group_chats = {}
		self.participants = {}
		self.admins = {}

	def create_group(self, user_id, group_name):
		group_id = len(self.groups) + 1
		self.groups[group_id] = group_name
		self.participants[group_id] = [user_id]
		return group_id

	def edit_group(self, user_id, group_id, new_group_name):
		if group_id in self.groups:
			self.groups[group_id] = new_group_name
			return True
		return False

	def create_group_chat(self, user_id, group_name, group_picture):
		group_chat_id = len(self.group_chats) + 1
		self.group_chats[group_chat_id] = {'name': group_name, 'picture': group_picture, 'participants': [user_id]}
		return group_chat_id

	def add_participant(self, group_id, participant_to_add):
		if group_id in self.participants and participant_to_add not in self.participants[group_id]:
			self.participants[group_id].append(participant_to_add)
			return True
		return False

	def remove_participant(self, group_id, participant_to_remove):
		if group_id in self.participants and participant_to_remove in self.participants[group_id]:
			self.participants[group_id].remove(participant_to_remove)
			return True
		return False

	def assign_admin(self, group_id, user_id):
		if group_id in self.participants and user_id in self.participants[group_id]:
			self.admins[group_id] = user_id
			return True
		return False

	def change_admin_permissions(self, group_id, user_id, new_permissions):
		if group_id in self.admins and self.admins[group_id] == user_id:
			self.admins[group_id] = {'user_id': user_id, 'permissions': new_permissions}
			return True
		return False
