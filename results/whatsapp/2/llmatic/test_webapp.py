import pytest
from webapp import WebApp
from user import User
from group import Group

def test_webapp():
	app = WebApp()

	# Test user registration and login
	user1 = app.register_user('user1@example.com', 'password1')
	user2 = app.register_user('user2@example.com', 'password2')
	app.login_user(user1)
	assert app.is_online(user1)
	assert not app.is_online(user2)

	# Test chat creation and messaging
	chat = app.create_chat(user1, user2)
	app.send_message(chat, user1, user2, 'Hello, world!')
	assert len(app.messages) == 1
	assert app.messages[0].content == 'Hello, world!'

	# Test group creation and user addition
	group = app.create_group('Test Group')
	app.add_user_to_group(user1, group)
	assert user1 in group.participants

	# Test status creation
	status = app.create_status(user1, 'Hello, world!')
	assert status in app.statuses
