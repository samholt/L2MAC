from models import User

def test_user_model():
	user = User('test_user', 'test_password', 'test_email')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.email == 'test_email'

	# Test create user
	new_user = user.create_user('new_user', 'new_password', 'new_email')
	assert new_user == {'password': 'new_password', 'email': 'new_email'}

	# Test update user
	updated_user = user.update_user('new_user', password='updated_password')
	assert updated_user == {'password': 'updated_password', 'email': 'new_email'}

	# Test delete user
	deleted = user.delete_user('new_user')
	assert deleted == True
