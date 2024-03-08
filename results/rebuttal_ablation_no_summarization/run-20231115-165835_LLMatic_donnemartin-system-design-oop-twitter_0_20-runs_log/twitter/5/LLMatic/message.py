import datetime


class Message:
	def __init__(self):
		self.messages = {}

	def send(self, sender, receiver, text):
		timestamp = datetime.datetime.now()
		message = {'sender': sender, 'receiver': receiver, 'text': text, 'timestamp': timestamp}
		if (sender, receiver) in self.messages:
			self.messages[(sender, receiver)].append(message)
		elif (receiver, sender) in self.messages:
			self.messages[(receiver, sender)].append(message)
		else:
			self.messages[(sender, receiver)] = [message]

	def view_thread(self, user1, user2):
		if (user1, user2) in self.messages:
			return self.messages[(user1, user2)]
		elif (user2, user1) in self.messages:
			return self.messages[(user2, user1)]
		else:
			return []
