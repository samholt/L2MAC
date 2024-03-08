from auth import Auth
from models import User


def test_auth():
	auth = Auth()

	# Test login with wrong credentials
	assert not auth.login('test_user', 'wrong_password')

	# Test login with correct credentials
	assert auth.login('test_user', 'test_password')

	# Test if user is logged in
	assert auth.logged_in_user == 'test_user'

	# Test logout
	auth.logout()
	assert auth.logged_in_user is None

	# Test register existing user
	assert not auth.register('test_user', 'test_password', 'test_email')

	# Test register new user
	# As we are mocking the database, the new user won't be saved
	# So we can use the same credentials every time
	assert auth.register('new_user', 'new_password', 'new_email')
