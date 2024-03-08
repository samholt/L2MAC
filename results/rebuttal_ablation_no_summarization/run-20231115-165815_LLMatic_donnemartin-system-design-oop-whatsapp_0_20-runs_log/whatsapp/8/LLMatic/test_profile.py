import pytest
from profile import Profile

def test_profile_features():
	profile = Profile()
	
	# Test setting profile picture
	profile.set_profile_picture('image_file.jpg')
	assert profile.view_profile()['profile_picture'] == 'image_file.jpg'
	
	# Test setting status message
	profile.set_status_message('Hello, world!')
	assert profile.view_profile()['status_message'] == 'Hello, world!'
	
	# Test configuring privacy settings
	privacy_settings = {'show_status': False, 'show_last_seen': False}
	profile.configure_privacy_settings(privacy_settings)
	assert profile.view_profile()['privacy_settings'] == privacy_settings
