import pytest
import random
from status_service import StatusService

status_service = StatusService()


def test_post_image_status():
	user_id = random.randint(1, 100)
	image_status = f"/path/to/status_image{random.randint(1, 5)}.jpg"
	duration = random.randint(1, 24)  # Hours
	assert status_service.post_image_status(user_id, image_status, duration) == True


def test_status_visibility():
	user_id = random.randint(1, 100)
	visibility_settings = random.choice(['Everyone', 'Contacts', 'Nobody'])
	assert status_service.set_status_visibility(user_id, visibility_settings) == True
