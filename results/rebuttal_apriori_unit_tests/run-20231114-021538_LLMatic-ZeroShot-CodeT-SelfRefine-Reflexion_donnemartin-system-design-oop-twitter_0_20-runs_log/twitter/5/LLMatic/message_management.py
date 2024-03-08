import datetime


class Message:
	def __init__(self, message_id, sender_id, receiver_id, content):
		self.message_id = message_id
		self.sender_id = sender_id
		self.receiver_id = receiver_id
		self.content = content
		self.timestamp = datetime.datetime.now()


messages = {}


def send_message(sender_id, receiver_id, content):
	message_id = len(messages) + 1
	messages[message_id] = Message(message_id, sender_id, receiver_id, content)
	return True
