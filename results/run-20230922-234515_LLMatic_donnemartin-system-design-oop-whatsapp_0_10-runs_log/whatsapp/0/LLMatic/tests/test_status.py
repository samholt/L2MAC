import pytest
from services.status import post_status, set_visibility
from models.status import Status
from utils.database import Database

db = Database()


def test_post_status():
	status = post_status('user1', 'image1', 'public')
	assert isinstance(status, Status)
	assert status.user_id == 'user1'
	assert status.image == 'image1'
	assert status.visibility == 'public'


def test_set_visibility():
	status = post_status('user1', 'image1', 'public')
	set_visibility('user1', 'private')
	status = db.get_status('user1')
	assert status.visibility == 'private'
