from models import User


def test_user_model():
	user = User('testuser', 'testpassword', 'testuser@test.com')
	assert user.username == 'testuser'
	assert user.email == 'testuser@test.com'
	assert user.check_password('testpassword')
	assert not user.check_password('wrongpassword')
