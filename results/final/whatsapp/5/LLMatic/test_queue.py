import pytest
from user import User
from message import Message
from queue import Queue


def test_queue():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	message1 = Message(user1, user2, 'Hello, User2!')
	message2 = Message(user1, user2, 'How are you?')

	queue = Queue(user2)
	queue.enqueue(message1)
	queue.enqueue(message2)

	assert len(queue.messages) == 2

	queue.send_all()
	assert len(queue.messages) == 0


def test_queue_functions():
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')
	message1 = Message(user1, user2, 'Hello, User2!')
	message2 = Message(user1, user2, 'How are you?')

	queue = Queue(user2)
	queue.enqueue(message1)
	queue.enqueue(message2)

	assert len(queue.messages) == 2

	dequeued_message = queue.dequeue()
	assert dequeued_message == message1
	assert len(queue.messages) == 1

	queue.send_all()
	assert len(queue.messages) == 0

if __name__ == '__main__':
	pytest.main(['-v', 'test_queue.py'])
