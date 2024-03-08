from datetime import datetime, timedelta
from user import User
from status import Status


def test_status():
	# Create users
	user1 = User('user1@example.com', 'password1')
	user2 = User('user2@example.com', 'password2')

	# Create status
	status = Status(user1, 'Hello, world!', [user2], datetime.now() + timedelta(hours=1))

	# Post status
	status.post()
	assert status in user1.status

	# View status
	assert status.view(user2) == 'Hello, world!'
	assert status.view(user1) is None

	# Delete status
	status.delete()
	assert status not in user1.status
