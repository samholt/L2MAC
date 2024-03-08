class BookClub:
	def __init__(self, name, description, is_private, admin):
		self.name = name
		self.description = description
		self.is_private = is_private
		self.members = [admin]
		self.admins = [admin]

	def create_club(self, name, description, is_private, admin):
		self.name = name
		self.description = description
		self.is_private = is_private
		self.members = [admin]
		self.admins = [admin]

	def update_club_info(self, name=None, description=None, is_private=None):
		if name:
			self.name = name
		if description:
			self.description = description
		if is_private is not None:
			self.is_private = is_private

	def add_member(self, user):
		if user not in self.members:
			self.members.append(user)

	def remove_member(self, user):
		if user in self.members:
			self.members.remove(user)

	def manage_member_requests(self, user, action):
		if action == 'approve':
			self.add_member(user)
		elif action == 'deny':
			self.remove_member(user)

	def manage_permissions(self, user, action):
		if action == 'promote' and user in self.members:
			self.admins.append(user)
		elif action == 'demote' and user in self.admins:
			self.admins.remove(user)
