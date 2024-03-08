import pytest
from user import User
from message import Message
from chat import Chat
from group_chat import GroupChat
from image_message import ImageMessage
from controller import Controller


def test_user():
	user = User('1', 'Alice')
	assert user.id == '1'
	assert user.name == 'Alice'


def test_message():
	message = Message('1', '1', '2', 'Hello')
	assert message.sender_id == '1'
	assert message.receiver_id == '2'
	assert message.content == 'Hello'
	assert message.status == 'sent'
	message.set_status('delivered')
	assert message.get_status() == 'delivered'
	message.encrypt_content()
	assert message.content != 'Hello'
	message.decrypt_content()
	assert message.content == 'Hello'


def test_chat():
	chat = Chat('1', ['1', '2'])
	assert chat.id == '1'
	assert chat.user_ids == ['1', '2']
	message = Message('1', '1', '2', 'Hello')
	chat.add_message(message)
	assert chat.get_chat_history() == [message]
	chat.mark_as_read('1')
	assert message.status == 'read'


def test_group_chat():
	group_chat = GroupChat('1', ['1', '2'])
	assert group_chat.id == '1'
	assert group_chat.user_ids == ['1', '2']
	group_chat.add_user('3')
	assert group_chat.user_ids == ['1', '2', '3']
	group_chat.remove_user('2')
	assert group_chat.user_ids == ['1', '3']


def test_image_message():
	image_message = ImageMessage('1', '1', '2', 'Hello', 'image_data')
	assert image_message.sender_id == '1'
	assert image_message.receiver_id == '2'
	assert image_message.content == 'Hello'
	assert image_message.image_data == 'image_data'
	assert image_message.status == 'sent'
	image_message.set_image_data('new_image_data')
	assert image_message.get_image_data() == 'new_image_data'


def test_controller():
	controller = Controller()
	user1 = controller.create_user('1', 'Alice')
	user2 = controller.create_user('2', 'Bob')
	user3 = controller.create_user('3', 'Charlie')
	assert user1.id == '1'
	assert user1.name == 'Alice'
	chat = controller.create_chat(['1', '2'])
	assert chat.id in user1.chats
	group_chat = controller.create_group_chat(['1', '2', '3'])
	assert group_chat.id in user1.chats
	message = controller.send_message('1', '2', chat.id, 'Hello')
	assert message in chat.messages
	image_message = controller.send_image_message('1', '2', chat.id, 'Hello', 'image_data')
	assert image_message in chat.messages
	assert controller.view_chat_history('1', chat.id) == chat.get_chat_history()

