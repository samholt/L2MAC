from user import User

def test_user_creation():
	user = User('test@example.com', 'password')
	assert user.email == 'test@example.com'
	assert user.check_password('password')

	user_dict = user.to_dict()
	assert 'id' in user_dict
	assert user_dict['email'] == 'test@example.com'
