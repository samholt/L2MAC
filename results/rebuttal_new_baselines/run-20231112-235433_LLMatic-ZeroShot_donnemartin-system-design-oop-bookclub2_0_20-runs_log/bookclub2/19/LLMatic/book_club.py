class BookClub:
	def __init__(self, club_id, name, privacy, members=[]):
		self.club_id = club_id
		self.name = name
		self.privacy = privacy
		self.members = members

	def create_club(self, club_id, name, privacy):
		self.club_id = club_id
		self.name = name
		self.privacy = privacy
		self.members = []

	def add_member(self, member):
		self.members.append(member)

	def update_club_info(self, name=None, privacy=None):
		if name is not None:
			self.name = name
		if privacy is not None:
			self.privacy = privacy
