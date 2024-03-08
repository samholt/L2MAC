from user import User
from message import Message

class Group:
	def __init__(self, name, picture, admin):
		self.name = name
		self.picture = picture
		self.participants = [admin]
		self.admin = admin

	def add_participant(self, user):
		if user not in self.participants:
			self.participants.append(user)
			return 'User added successfully'
		return 'User already in the group'

	def remove_participant(self, user):
		if user in self.participants:
			self.participants.remove(user)
			return 'User removed successfully'
		return 'User not in the group'

	def set_admin(self, user):
		if user in self.participants:
			self.admin = user
			return 'Admin set successfully'
		return 'User not in the group'

	def send_message(self, content, db):
		message = Message(self.admin, self, content)
		message_id = message.send(db)
		return message_id
