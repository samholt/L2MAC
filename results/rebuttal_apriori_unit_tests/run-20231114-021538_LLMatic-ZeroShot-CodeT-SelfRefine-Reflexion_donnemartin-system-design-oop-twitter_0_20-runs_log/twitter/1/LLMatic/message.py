class Message:
	def __init__(self, id, sender_id, receiver_id, content):
		self.id = id
		self.sender_id = sender_id
		self.receiver_id = receiver_id
		self.content = content

mock_db = {}


def send_message(sender_id, receiver_id, content):
	message_id = len(mock_db) + 1
	message = Message(message_id, sender_id, receiver_id, content)
	mock_db[message_id] = message
	return True
