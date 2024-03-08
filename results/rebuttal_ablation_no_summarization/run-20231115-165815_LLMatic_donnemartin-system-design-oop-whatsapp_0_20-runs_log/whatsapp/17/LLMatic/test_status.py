import pytest
from auth import Auth
from profile import Profile
from status import Status


def test_status():
	auth = Auth()
	auth.signup('user1', 'password1')
	profile = Profile('user1')
	status = Status(profile)
	assert status.post_status('Online') == True
