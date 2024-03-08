import pytest
from cloudsafe.models.user import User
from cloudsafe.controllers.log_controller import log_activity, activity_log_db

def test_log_activity():
	"""Tests the log_activity function."""
	user = User(id='1', name='Test User', email='test@example.com', password='password', profile_picture='', storage_used=0, storage_limit=1000)
	activity = 'Uploaded a file'
	log_activity(user, activity)
	assert activity_log_db[user.id][0] == activity
