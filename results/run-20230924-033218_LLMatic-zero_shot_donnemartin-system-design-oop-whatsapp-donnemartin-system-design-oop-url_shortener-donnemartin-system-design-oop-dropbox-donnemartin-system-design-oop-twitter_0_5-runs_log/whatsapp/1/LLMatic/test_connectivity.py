from connectivity import connectivity, restore_connectivity
from message import Message
from status import Status
from user import User
import time

def test_connectivity():
	assert isinstance(connectivity(), bool)


def test_restore_connectivity():
	queue = []
	mock_db = {}
	message = Message('sender@test.com', 'receiver@test.com', 'Hello!')
	status = Status(User('user@test.com', 'password'), 'Hello, world!', 'public', 24)
	queue.append((message.send, [mock_db]))
	queue.append((status.post, [mock_db]))
	mock_db = restore_connectivity(queue, mock_db)
	time.sleep(2)  # wait for a second to allow the restore_connectivity function to process the queue
	assert len(mock_db) == 2
