import pytest
from models import User, Message, Chat, GroupChat, ImageMessage
from controller import Controller
from view import View


def test_user():
	user = User(id='1', name='Alice', chats=[])
	assert user.id == '1'
	assert user.name == 'Alice'
	assert user.chats == []


def test_message():
	alice = User(id='1', name='Alice', chats=[])
	message = Message(id='1', content='Hello, Bob!', sender=alice, status='sent')
	assert message.id == '1'
	assert message.content == 'Hello, Bob!'
	assert message.sender == alice
	assert message.status == 'sent'


def test_chat():
	alice = User(id='1', name='Alice', chats=[])
	bob = User(id='2', name='Bob', chats=[])
	chat = Chat(id='1', users=[alice, bob], messages=[])
	assert chat.id == '1'
	assert chat.users == [alice, bob]
	assert chat.messages == []


def test_group_chat():
	alice = User(id='1', name='Alice', chats=[])
	bob = User(id='2', name='Bob', chats=[])
	charlie = User(id='3', name='Charlie', chats=[])
	group_chat = GroupChat(id='1', users=[alice, bob, charlie], messages=[])
	assert group_chat.id == '1'
	assert group_chat.users == [alice, bob, charlie]
	assert group_chat.messages == []


def test_image_message():
	alice = User(id='1', name='Alice', chats=[])
	image_message = ImageMessage(id='1', content='', sender=alice, status='sent', image_path='path/to/image.jpg')
	assert image_message.id == '1'
	assert image_message.content == ''
	assert image_message.sender == alice
	assert image_message.status == 'sent'
	assert image_message.image_path == 'path/to/image.jpg'


def test_controller():
	controller = Controller()
	alice = controller.create_user(id='1', name='Alice')
	bob = controller.create_user(id='2', name='Bob')
	assert alice in controller.users.values()
	assert bob in controller.users.values()


def test_view():
	view = View()
	alice = view.create_user(id='1', name='Alice')
	bob = view.create_user(id='2', name='Bob')
	assert alice in view.controller.users.values()
	assert bob in view.controller.users.values()

