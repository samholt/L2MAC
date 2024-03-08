from typing import Union
from models.user import User
from models.message import Message


class MessageController:
	def __init__(self):
		self.messages = []
		self.message_queue = []

	def send_message(self, sender: User, receiver: Union[User, str], content: Union[str, bytes]):
		message = Message(id='message_id', sender=sender, receiver=receiver, content=content, read_receipt=False)
		if receiver.online_status:
			self.messages.append(message)
			# This is a placeholder for end-to-end encryption. In a real application, you would integrate with an encryption service.
			encrypted_content = 'encrypted_content'
			print(f'Sent message with encrypted content: {encrypted_content}')
		else:
			self.message_queue.append(message)

	def receive_message(self, message: Message):
		# This is a placeholder for end-to-end decryption. In a real application, you would integrate with an encryption service.
		decrypted_content = 'decrypted_content'
		print(f'Received message with decrypted content: {decrypted_content}')
		message.read_receipt = True

	def process_message_queue(self):
		for message in self.message_queue:
			if message.receiver.online_status:
				self.send_message(message.sender, message.receiver, message.content)
				self.message_queue.remove(message)
