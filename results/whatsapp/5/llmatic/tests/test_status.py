import pytest
from models.user import User
from models.status import Status
from controllers.status_controller import StatusController

def test_status():
	user1 = User(id='1', email='user1@example.com', password='password', profile_picture='picture.jpg', status_message='Hello', privacy_settings={}, blocked_contacts=[])
	user2 = User(id='2', email='user2@example.com', password='password', profile_picture='picture.jpg', status_message='Hello', privacy_settings={}, blocked_contacts=[])
	status_controller = StatusController()
	status_controller.post_status(user1, 'This is a status', {'blocked': [user2]})
	assert len(status_controller.statuses) == 1
	assert status_controller.statuses[0].content == 'This is a status'
	visible_statuses = status_controller.view_status(user2)
	assert len(visible_statuses) == 0
