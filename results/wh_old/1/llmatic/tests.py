from models.user import User
from models.chat import Chat
from models.group_chat import GroupChat
from models.message import Message
from models.image_message import ImageMessage
from controller.controller import Controller
import pytest


def test_user():
	user = User('user')
	assert user.username == 'user'
	assert user.chats == []

	chat = Chat([user])
	user.chats.append(chat)
	assert user.chats == [chat]


def test_message():
	sender = User('sender')
	chat = Chat([sender])
	message = Message(sender, chat, 'Hello')
	assert message.sender == sender
	assert message.chat == chat
	assert message.content == 'Hello'
	assert message.status == 'sent'

	message.set_status('delivered')
	assert message.status == 'delivered'

	message.encrypt_content()
	encrypted_content = message.content
	assert encrypted_content != 'Hello'

	message.decrypt_content()
	assert message.content == 'Hello'


def test_chat():
	user1 = User('user1')
	user2 = User('user2')
	chat = Chat([user1, user2])
	assert chat.users == [user1, user2]
	assert chat.messages == []

	message = Message(user1, chat, 'Hello')
	chat.add_message(message)
	assert chat.messages == [message]

	assert chat.get_chat_history() == [(user1, 'Hello')]


def test_group_chat():
	user1 = User('user1')
	user2 = User('user2')
	user3 = User('user3')
	group_chat = GroupChat([user1, user2, user3])
	assert group_chat.users == [user1, user2, user3]

	group_chat.remove_user(user2)
	assert group_chat.users == [user1, user3]

	group_chat.add_user(user2)
	assert group_chat.users == [user1, user3, user2]


def test_image_message():
	sender = User('sender')
	chat = Chat([sender])
	image_message = ImageMessage(sender, chat, 'image.jpg')
	assert image_message.sender == sender
	assert image_message.chat == chat
	assert image_message.image_path == 'image.jpg'

	# Mock the image reading functionality
	image_message.image_data = 'SGVsbG8='  # Base64 encoded string for 'Hello'
	image_data = image_message.image_data
	assert image_data is not None

	image_message.encrypt_content()
	encrypted_image_data = image_message.image_data
	assert encrypted_image_data != image_data

	image_message.decrypt_content('output.jpg')
	assert image_message.image_data == image_data


def test_controller():
	controller = Controller()
	assert controller.users == {}

	user1 = controller.create_user('user1')
	assert user1.username == 'user1'
	assert controller.users == {'user1': user1}

	user2 = controller.create_user('user2')
	assert user2.username == 'user2'
	assert controller.users == {'user1': user1, 'user2': user2}

	chat = controller.create_chat(['user1', 'user2'])
	assert chat.users == [user1, user2]

	controller.send_message('user1', chat, 'Hello')
	assert chat.messages[0].content == 'Hello'

	controller.receive_message('user2', chat.messages[0])
	assert chat.messages[0].status == 'delivered'

	chat_history = controller.view_chat_history('user1', chat)
	# Compare usernames instead of user objects
	assert chat_history == [(user1.username, 'Hello', 'delivered')]

	group_chat = controller.create_group_chat('user1', ['user2'])
	assert group_chat.users == [user1, user2]

	# Mock the image sending functionality
	controller.send_image('user1', chat, 'mock_image.jpg')
	assert isinstance(chat.messages[-1], ImageMessage)

if __name__ == '__main__':
	pytest.main()


