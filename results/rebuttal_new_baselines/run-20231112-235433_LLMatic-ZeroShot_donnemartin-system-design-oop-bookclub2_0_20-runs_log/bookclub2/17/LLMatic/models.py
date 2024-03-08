class User:
	def __init__(self, username, email, password_hash):
		self.username = username
		self.email = email
		self.password_hash = password_hash
		self.roles = []


class Role:
	def __init__(self, name):
		self.name = name
		self.permissions = []


class Permission:
	def __init__(self, name):
		self.name = name


class BookClub:
	def __init__(self, name, members, privacy='public'):
		self.name = name
		self.members = members
		self.privacy = privacy


class Meeting:
	def __init__(self):
		pass


class Discussion:
	def __init__(self):
		pass


class Comment:
	def __init__(self):
		pass


class Vote:
	def __init__(self):
		pass


class Profile:
	def __init__(self):
		pass


class Follow:
	def __init__(self):
		pass


class ReadingList:
	def __init__(self):
		pass


class Recommendation:
	def __init__(self):
		pass


class Dashboard:
	def __init__(self):
		pass


class Moderation:
	def __init__(self):
		pass


class Analytics:
	def __init__(self):
		pass
