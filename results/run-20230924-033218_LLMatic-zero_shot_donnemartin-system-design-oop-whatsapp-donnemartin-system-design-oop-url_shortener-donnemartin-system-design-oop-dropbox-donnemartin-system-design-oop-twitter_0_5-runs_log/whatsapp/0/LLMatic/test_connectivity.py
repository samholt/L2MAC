from connectivity import Connectivity
from user import User
from message import Message


def test_go_online():
	user = User('test@test.com', 'password')
	connectivity = Connectivity(user)
	connectivity.go_online()
	assert connectivity.online is True


def test_go_offline():
	user = User('test@test.com', 'password')
	connectivity = Connectivity(user)
	connectivity.go_offline()
	assert connectivity.online is False


def test_update_last_seen():
	user = User('test@test.com', 'password')
	connectivity = Connectivity(user)
	last_seen_before = connectivity.last_seen
	connectivity.update_last_seen()
	assert connectivity.last_seen > last_seen_before


def test_queue_message():
	user = User('test@test.com', 'password')
	connectivity = Connectivity(user)
	message = Message(user, user, 'Hello World')
	connectivity.queue_message(message)
	assert len(connectivity.message_queue) == 1


def test_send_queued_messages():
	user = User('test@test.com', 'password')
	connectivity = Connectivity(user)
	message = Message(user, user, 'Hello World')
	connectivity.queue_message(message)
	connectivity.go_online()
	connectivity.send_queued_messages()
	assert len(connectivity.message_queue) == 0
