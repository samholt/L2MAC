from services.user_service import register_user, get_user, update_user, delete_user
from services.post_service import create_post, get_post, delete_post
from services.message_service import send_message, get_message
from services.notification_service import create_notification, get_notification

def test_user_service():
	user = register_user('test', 'test@test.com', 'password')
	assert user.name == 'test'
	assert get_user('test@test.com') == user
	update_user('test@test.com', name='updated')
	assert user.name == 'updated'
	delete_user('test@test.com')
	assert get_user('test@test.com') is None

def test_post_service():
	user = register_user('test', 'test@test.com', 'password')
	post = create_post(user, 'Hello, world!')
	assert post.user == user
	assert get_post(user) == post
	delete_post(user)
	assert get_post(user) is None

def test_message_service():
	sender = register_user('sender', 'sender@test.com', 'password')
	receiver = register_user('receiver', 'receiver@test.com', 'password')
	message = send_message(sender, receiver, 'Hello, world!')
	assert message.sender == sender
	assert get_message(sender, receiver) == message

def test_notification_service():
	user = register_user('test', 'test@test.com', 'password')
	notification = create_notification(user, 'You have a new follower.')
	assert notification.user == user
	assert get_notification(user) == notification
