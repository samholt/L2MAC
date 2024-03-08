class BookClub:
	def __init__(self, name, privacy_settings, members, administrators):
		self.name = name
		self.privacy_settings = privacy_settings
		self.members = members
		self.administrators = administrators

	def create_club(self, name, privacy_settings, administrators):
		self.name = name
		self.privacy_settings = privacy_settings
		self.members = []
		self.administrators = administrators

	def add_member(self, member):
		self.members.append(member)

	def remove_member(self, member):
		self.members.remove(member)

	def update_privacy_settings(self, privacy_settings):
		self.privacy_settings = privacy_settings
