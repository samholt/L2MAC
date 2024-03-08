from controllers.direct_message_controller import DirectMessageController


class DirectMessageView:
	def __init__(self, controller: DirectMessageController):
		self.controller = controller

	def send_direct_message(self, sender, receiver, message: str):
		self.controller.send_direct_message(sender, receiver, message)
		print(f'Successfully sent direct message from {sender.username} to {receiver.username}')

	def view_direct_messages(self, user):
		direct_messages = self.controller.get_direct_messages(user)
		for direct_message in direct_messages:
			print(f'From: {direct_message.sender.username}, To: {direct_message.receiver.username}, Message: {direct_message.message}')
