import pytest
from user import User
from chat import Chat
from message import Message
from group import Group
from status import Status
from webapp import WebApp


def test_integration():
	# Create a web app
	app = WebApp()

	# Register two users
	app.register_user('user1@example.com', 'password1')
	app.register_user('user2@example.com', 'password2')

	# Login the users
	user1 = app.login_user('user1@example.com', 'password1')
	user2 = app.login_user('user2@example.com', 'password2')

	# Send a message from user1 to user2
	app.send_message('user1@example.com', 'user2@example.com', 'Hello, user2!', 'text')

	# Check that the message was sent
	chat = app.get_chat_by_users(user1, user2)
	assert chat is not None
	assert len(chat.messages) == 1
	assert chat.messages[0][2].content == 'Hello, user2!'

	# Check that the message was not read
	assert not chat.read_receipts[('user1@example.com', 'user2@example.com', 'Hello, user2!')]

	# Receive the message as user2
	message = chat.receive_message(user1, user2, chat.messages[0][2])

	# Check that the message was received
	assert message is not None
	assert message.content == 'Hello, user2!'

	# Check that the message was marked as read
	assert chat.read_receipts[('user1@example.com', 'user2@example.com', 'Hello, user2!')]

	# Create a group with user1 as admin
	group = Group()
	group.create_group('Group1', 'group_picture.jpg', user1)

	# Add user2 to the group
	group.add_participant(user2)

	# Check that user2 was added to the group
	assert len(group.participants) == 2
	assert any(u.email == 'user2@example.com' for u in group.participants)

	# Post a status as user1
	status = Status()
	status.post_status(user1, 'status_image.jpg', 'public')

	# Check that the status is visible
	assert status.is_visible()

	# Logout user1
	user1.logout()

	# Check that user1 is offline
	assert not app.display_status('user1@example.com')

	# Restore connectivity for user1
	app.restore_connectivity('user1@example.com')

	# Check that user1 is online
	assert app.display_status('user1@example.com')


if __name__ == '__main__':
	pytest.main(['-v', 'test_integration.py'])

