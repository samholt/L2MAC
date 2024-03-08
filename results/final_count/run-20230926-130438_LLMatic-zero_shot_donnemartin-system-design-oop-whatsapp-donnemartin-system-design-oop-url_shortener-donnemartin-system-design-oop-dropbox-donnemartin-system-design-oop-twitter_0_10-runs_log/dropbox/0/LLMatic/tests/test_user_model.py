from models.User import User

def test_user_model():
	user = User(1, 'Test User', 'test@example.com', 'password', 'profile.jpg', 0)
	assert user.id == 1
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.password == 'password'
	assert user.profile_picture == 'profile.jpg'
	assert user.storage_used == 0
	assert user.__repr__() == 'User(1, Test User, test@example.com, password, profile.jpg, 0)'
	assert user.to_dict() == {
		'id': 1,
		'name': 'Test User',
		'email': 'test@example.com',
		'password': 'password',
		'profile_picture': 'profile.jpg',
		'storage_used': 0
	}
