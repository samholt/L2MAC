class GroupChat:
	def __init__(self, group_name, group_picture, participants):
		self.group_name = group_name
		self.group_picture = group_picture
		self.participants = participants
		self.admins = [participants[0]]

	def create_group_chat(self):
		return {'group_name': self.group_name, 'group_picture': self.group_picture, 'participants': self.participants, 'admins': self.admins}

	def add_participant(self, participant):
		self.participants.append(participant)

	def remove_participant(self, participant):
		self.participants.remove(participant)

	def manage_admin_roles(self, admin, action):
		if action == 'add':
			self.admins.append(admin)
		elif action == 'remove':
			self.admins.remove(admin)
		return self.admins
