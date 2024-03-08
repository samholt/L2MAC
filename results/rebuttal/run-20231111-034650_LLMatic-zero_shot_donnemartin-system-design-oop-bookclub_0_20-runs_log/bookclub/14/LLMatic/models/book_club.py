from models.user import User

class BookClub:
	def __init__(self, id, name, description, privacy, members, current_book):
		self.id = id
		self.name = name
		self.description = description
		self.privacy = privacy
		self.members = members if members else []
		self.current_book = current_book

	def create_club(self, name, description, privacy):
		self.name = name
		self.description = description
		self.privacy = privacy
		self.members = []
		self.current_book = None

	def add_member(self, member):
		if isinstance(member, User):
			self.members.append(member)

	def update_info(self, name=None, description=None, privacy=None, current_book=None):
		if name:
			self.name = name
		if description:
			self.description = description
		if privacy:
			self.privacy = privacy
		if current_book:
			self.current_book = current_book
