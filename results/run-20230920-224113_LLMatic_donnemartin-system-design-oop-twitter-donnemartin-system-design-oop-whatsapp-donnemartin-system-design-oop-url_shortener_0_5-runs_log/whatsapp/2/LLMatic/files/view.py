from controller import Controller


class View:
	def __init__(self, controller):
		self.controller = controller

	def display_chat_history(self, user_id, chat_id):
		chat_history = self.controller.view_chat_history(user_id, chat_id)
		for message in chat_history:
			print(f'{message.sender_id}: {message.content}')
			if message.status == 'delivered':
				print('Status: Delivered')
			elif message.status == 'read':
				print('Status: Read')

	def handle_user_input(self):
		while True:
			print('Enter command:')
			command = input()
			if command == 'quit':
				break
			elif command.startswith('send message'):
				_, sender_id, receiver_id, chat_id, content = command.split()
				self.controller.send_message(sender_id, receiver_id, chat_id, content)
			elif command.startswith('send image message'):
				_, sender_id, receiver_id, chat_id, content, image_data = command.split()
				self.controller.send_image_message(sender_id, receiver_id, chat_id, content, image_data)
			elif command.startswith('view chat history'):
				_, user_id, chat_id = command.split()
				self.display_chat_history(user_id, chat_id)
			else:
				print('Invalid command')

