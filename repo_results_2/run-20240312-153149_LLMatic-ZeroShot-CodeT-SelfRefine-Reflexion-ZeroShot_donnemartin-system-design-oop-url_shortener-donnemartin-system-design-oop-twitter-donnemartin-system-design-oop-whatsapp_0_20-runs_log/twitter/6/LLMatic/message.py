import datetime


class Message:
	def __init__(self):
		self.database = {}

	def send(self, sender, receiver, content):
		timestamp = datetime.datetime.now()
		message_id = len(self.database) + 1
		self.database[message_id] = {'sender': sender, 'receiver': receiver, 'content': content, 'timestamp': timestamp}
		return message_id

	def block(self, blocker, blockee):
		if blocker not in self.database:
			self.database[blocker] = {'blocked': [blockee]}
		else:
			self.database[blocker]['blocked'].append(blockee)
		return True
