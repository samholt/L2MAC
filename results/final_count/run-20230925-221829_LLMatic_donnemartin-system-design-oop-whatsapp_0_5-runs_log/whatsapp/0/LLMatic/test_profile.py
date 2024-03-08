import profile

def test_set_profile_picture():
	user_profile = profile.UserProfile()
	user_profile.set_profile_picture('user1', 'image1.jpg')
	assert user_profile.database['user1']['profile_picture'] == 'image1.jpg'

def test_set_status_message():
	user_profile = profile.UserProfile()
	user_profile.set_status_message('user1', 'Hello, world!')
	assert user_profile.database['user1']['status_message'] == 'Hello, world!'

def test_manage_privacy_settings():
	user_profile = profile.UserProfile()
	user_profile.manage_privacy_settings('user1', 'private')
	assert user_profile.database['user1']['privacy_setting'] == 'private'
