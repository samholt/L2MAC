import auth


def test_register():
	user = auth.register('testuser', 'testuser@example.com', 'password')
	assert user.username == 'testuser'
	assert user.email == 'testuser@example.com'
	assert user.check_password('password')


def test_authenticate():
	token = auth.authenticate('testuser', 'password')
	assert token is not None


def test_edit_profile():
	user = auth.edit_profile('testuser', 'new_picture.jpg', 'This is a bio.', 'http://example.com', 'Location')
	assert user.profile_picture == 'new_picture.jpg'
	assert user.bio == 'This is a bio.'
	assert user.website_link == 'http://example.com'
	assert user.location == 'Location'

