class GroupChat:
	def __init__(self):
		self.group_chats = {}

	def create_group_chat(self, user_id, group_name, group_picture, participant_ids):
		group_chat_id = len(self.group_chats) + 1
		self.group_chats[group_chat_id] = {
			'admin': user_id,
			'name': group_name,
			'picture': group_picture,
			'participants': participant_ids,
			'roles': {user_id: 'admin'}
		}
		return group_chat_id

	def add_participant(self, group_chat_id, participant_id):
		self.group_chats[group_chat_id]['participants'].append(participant_id)

	def remove_participant(self, group_chat_id, participant_id):
		self.group_chats[group_chat_id]['participants'].remove(participant_id)

	def manage_roles(self, group_chat_id, user_id, role):
		self.group_chats[group_chat_id]['roles'][user_id] = role
