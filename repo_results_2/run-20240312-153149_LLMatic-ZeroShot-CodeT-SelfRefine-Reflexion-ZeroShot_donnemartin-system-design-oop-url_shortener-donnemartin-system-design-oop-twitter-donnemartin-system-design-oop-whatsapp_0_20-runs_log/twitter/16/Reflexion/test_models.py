from models.user import User
from models.post import Post
from models.message import Message
from models.notification import Notification

def test_user_creation():
	user = User('test', 'test@test.com', 'password')
	assert user.name == 'test'
	assert user.email == 'test@test.com'
	assert user.password == 'password'

def test_post_creation():
	user = User('test', 'test@test.com', 'password')
	post = Post(user, 'Hello, world!')
	assert post.user == user
	assert post.content == 'Hello, world!'

def test_message_creation():
	sender = User('sender', 'sender@test.com', 'password')
	receiver = User('receiver', 'receiver@test.com', 'password')
	message = Message(sender, receiver, 'Hello, world!')
	assert message.sender == sender
	assert message.receiver == receiver
	assert message.content == 'Hello, world!'

def test_notification_creation():
	user = User('test', 'test@test.com', 'password')
	notification = Notification(user, 'You have a new follower.')
	assert notification.user == user
	assert notification.content == 'You have a new follower.'
