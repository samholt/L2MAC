class MessageService:
	def __init__(self):
		self.messages = {}
		self.message_id_counter = 0

	def send_message(self, sender_id, receiver_id, message):
		self.message_id_counter += 1
		self.messages[self.message_id_counter] = {'sender': sender_id, 'receiver': receiver_id, 'content': message, 'read': False}
		return self.message_id_counter

	def receive_message(self, receiver_id):
		for message_id, message in self.messages.items():
			if message['receiver'] == receiver_id:
				return message['content']
		return None

	def mark_as_read(self, receiver_id, message_id):
		if message_id not in self.messages or self.messages[message_id]['receiver'] != receiver_id:
			return False
		self.messages[message_id]['read'] = True
		return True

	def encrypt_message(self, sender_id, message):
		return ''.join(chr(ord(c) + 1) for c in message)

	def decrypt_message(self, receiver_id, encrypted_message):
		return ''.join(chr(ord(c) - 1) for c in encrypted_message)

	def send_image(self, sender_id, receiver_id, image_path):
		self.message_id_counter += 1
		self.messages[self.message_id_counter] = {'sender': sender_id, 'receiver': receiver_id, 'content': image_path, 'read': False}
		return self.message_id_counter

	def receive_image(self, receiver_id):
		for message_id, message in self.messages.items():
			if message['receiver'] == receiver_id:
				return message['content']
		return None

	def send_content(self, sender_id, receiver_id, content):
		self.message_id_counter += 1
		self.messages[self.message_id_counter] = {'sender': sender_id, 'receiver': receiver_id, 'content': content, 'read': False}
		return self.message_id_counter

	def receive_content(self, receiver_id):
		for message_id, message in self.messages.items():
			if message['receiver'] == receiver_id:
				return message['content']
		return None
