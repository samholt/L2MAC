import pytest
from app.models import User, Status
from app.views import users_db, statuses_db
from datetime import datetime, timedelta


def test_status():
	# Create a user
	user = User.create(id=1, email='user@example.com', password='test', profile_picture='user.jpg', status_message='Hello, world!', privacy_settings='Public', last_seen='2022-01-01 00:00:00', contacts=[], blocked_contacts=[])
	users_db[user.id] = user

	# Post a status
	status = Status.create(id=1, user='user', content='This is a status!', visibility='Public', expiry_time=datetime.utcnow() + timedelta(hours=24))
	statuses_db[status.id] = status
	assert status in statuses_db.values()

	# View statuses
	statuses = [status for status in statuses_db.values() if status.user == 'user' and status.expiry_time > datetime.utcnow()]
	assert status in statuses

	# Change status visibility
	status.visibility = 'Private'
	assert status.visibility == 'Private'

	# Check that the status disappears after the time limit
	status.expiry_time = datetime.utcnow() - timedelta(minutes=1)  # Set the expiry time to 1 minute ago
	statuses = [status for status in statuses_db.values() if status.user == 'user' and status.expiry_time > datetime.utcnow()]
	assert status not in statuses
