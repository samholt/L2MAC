from cloudsafe.models.user import User

def test_user_model():
	user = User(id='1', name='Test User', email='test@example.com', password='password', profile_picture='http://example.com/profile.jpg', storage_used=0, storage_limit=1000)
	assert user.id == '1'
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.password == 'password'
	assert user.profile_picture == 'http://example.com/profile.jpg'
	assert user.storage_used == 0
	assert user.storage_limit == 1000
