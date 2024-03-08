import pytest
import status

status_service = status.StatusService()

@pytest.mark.parametrize('user_id, image_status, duration', [(1, '/path/to/status_image1.jpg', 5), (2, '/path/to/status_image2.jpg', 10)])
def test_post_image_status(user_id, image_status, duration):
	assert status_service.post_image_status(user_id, image_status, duration) == True

@pytest.mark.parametrize('user_id, visibility', [(1, 'Everyone'), (2, 'Contacts')])
def test_set_status_visibility(user_id, visibility):
	assert status_service.set_status_visibility(user_id, visibility) == True
