class BookClub:
	def __init__(self, id, name, privacy_settings):
		self.id = id
		self.name = name
		self.privacy_settings = privacy_settings
		self.members = []

	def create_club(self, id, name, privacy_settings):
		self.id = id
		self.name = name
		self.privacy_settings = privacy_settings

	def add_member(self, user):
		self.members.append(user)

	def remove_member(self, user):
		if user in self.members:
			self.members.remove(user)

	def get_club_info(self):
		return {'id': self.id, 'name': self.name, 'privacy_settings': self.privacy_settings, 'members': [member.get_info() for member in self.members]}
