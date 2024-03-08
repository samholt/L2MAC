import pytest
from models.user import User
from models.direct_message import DirectMessage
from controllers.user_controller import UserController
from controllers.direct_message_controller import DirectMessageController


def test_direct_message_creation():
	user_controller = UserController()
	direct_message_controller = DirectMessageController()
	user1 = user_controller.create_user('user1', 'password1')
	user2 = user_controller.create_user('user2', 'password2')
	direct_message = direct_message_controller.send_direct_message(user1, user2, 'Hello, user2!')
	assert direct_message.sender == user1
	assert direct_message.receiver == user2
	assert direct_message.message == 'Hello, user2!'
