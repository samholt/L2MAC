from dataclasses import dataclass
from user import User

@dataclass
class Group:
	def __init__(self):
		self.name = None
		self.picture = None
		self.participants = []
		self.admins = []

	def create_group(self, name, picture, admin):
		self.name = name
		self.picture = picture
		self.admins.append(admin)
		self.participants.append(admin)

	def add_participant(self, user):
		if not any(u.email == user.email for u in self.participants):
			self.participants.append(user)

	def remove_participant(self, user):
		self.participants = [u for u in self.participants if u.email != user.email]

	def add_admin(self, user):
		if any(u.email == user.email for u in self.participants) and not any(u.email == user.email for u in self.admins):
			self.admins.append(user)

	def remove_admin(self, user):
		self.admins = [u for u in self.admins if u.email != user.email]
		if not any(u.email == user.email for u in self.participants):
				self.participants.append(user)
