from message import Message
from user import User


def test_send_offline():
	user1 = User('test1@test.com', 'password')
	user2 = User('test2@test.com', 'password')
	message = Message(user1, user2, 'Hello')
	message.send_offline()
	assert len(message.queue) == 1
	user1.set_online_status(True)
	message.send_offline()
	assert len(message.queue) == 0
