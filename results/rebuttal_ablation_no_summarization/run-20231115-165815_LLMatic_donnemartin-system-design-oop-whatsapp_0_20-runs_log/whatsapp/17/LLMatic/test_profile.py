from profile import Profile


def test_profile_creation():
	profile = Profile('testuser')
	assert profile.username == 'testuser'
	assert profile.profile_picture == None
	assert profile.status_message == None
	assert profile.privacy_settings == {'view_profile_picture': 'everyone', 'view_status_message': 'everyone'}


def test_set_profile_picture():
	profile = Profile('testuser')
	profile.set_profile_picture('picture.jpg')
	assert profile.profile_picture == 'picture.jpg'


def test_set_status_message():
	profile = Profile('testuser')
	profile.set_status_message('Hello, world!')
	assert profile.status_message == 'Hello, world!'


def test_set_privacy_settings():
	profile = Profile('testuser')
	profile.set_privacy_settings('view_profile_picture', 'friends')
	assert profile.privacy_settings['view_profile_picture'] == 'friends'
