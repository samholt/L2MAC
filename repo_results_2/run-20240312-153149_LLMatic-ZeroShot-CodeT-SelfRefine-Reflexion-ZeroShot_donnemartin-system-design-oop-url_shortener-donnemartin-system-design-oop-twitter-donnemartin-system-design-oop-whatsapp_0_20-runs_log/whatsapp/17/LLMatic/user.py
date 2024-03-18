from group_chat import GroupChat

class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.contacts = {}
		self.groups = {}

	def create_group(self, group_name):
		if group_name not in self.groups:
			self.groups[group_name] = GroupChat(group_name, self.email)

	def add_to_group(self, group_name, email):
		if group_name in self.groups:
			self.groups[group_name].add_participant(email)

	def remove_from_group(self, group_name, email):
		if group_name in self.groups:
			self.groups[group_name].remove_participant(email)

	def set_group_admin(self, group_name, email):
		if group_name in self.groups:
			self.groups[group_name].add_admin(email)

	def remove_group_admin(self, group_name, email):
		if group_name in self.groups:
			self.groups[group_name].remove_admin(email)
