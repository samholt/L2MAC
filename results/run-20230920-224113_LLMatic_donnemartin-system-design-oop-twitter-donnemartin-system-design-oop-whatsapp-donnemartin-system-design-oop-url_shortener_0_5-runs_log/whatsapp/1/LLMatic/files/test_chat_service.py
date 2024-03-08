import pytest
from models import User, Message, Chat, GroupChat, ImageMessage
from controller import Controller
from view import View


def test_user():
	user = User('test_user')
	assert user.username == 'test_user'
	assert user.chats == []


def test_message():
	message = Message('test_user', 'Hello, World!')
	assert message.sender == 'test_user'
	assert message.content == 'Hello, World!'
	assert message.delivered == False
	assert message.read == False


def test_chat():
	chat = Chat(['test_user1', 'test_user2'])
	assert chat.users == ['test_user1', 'test_user2']
	assert chat.messages == []


def test_group_chat():
	group_chat = GroupChat(['test_user1', 'test_user2', 'test_user3'])
	assert group_chat.users == ['test_user1', 'test_user2', 'test_user3']


def test_image_message():
	image_message = ImageMessage('test_user', 'image_content')
	assert image_message.sender == 'test_user'
	assert image_message.content == 'image_content'


def test_controller():
	controller = Controller()
	user = controller.create_user('test_user')
	assert user.username == 'test_user'
	assert controller.users == {'test_user': user}


def test_view():
	controller = Controller()
	view = View(controller)
	assert view.controller == controller

