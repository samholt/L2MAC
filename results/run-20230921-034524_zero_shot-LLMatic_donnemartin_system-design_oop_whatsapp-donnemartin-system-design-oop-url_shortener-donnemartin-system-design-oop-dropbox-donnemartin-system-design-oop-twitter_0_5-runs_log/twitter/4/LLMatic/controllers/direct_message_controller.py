from models.direct_message import DirectMessage


class DirectMessageController:
	def __init__(self):
		self.direct_messages = []

	def send_direct_message(self, sender, receiver, message: str):
		direct_message = DirectMessage(sender, receiver, message)
		self.direct_messages.append(direct_message)
		return direct_message

	def get_direct_messages(self, user):
		messages = []
		for direct_message in self.direct_messages:
			if direct_message.sender == user or direct_message.receiver == user:
				messages.append(direct_message)
		return messages
