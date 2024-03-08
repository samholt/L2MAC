from services.user_service import UserService
import hashlib

def test_register_user():
	UserService.register_user('test', 'test@test.com', 'password')
	assert 'test@test.com' in UserService.users_db
	assert UserService.users_db['test@test.com'].name == 'test'
	assert UserService.users_db['test@test.com'].email == 'test@test.com'
	assert UserService.users_db['test@test.com'].password == hashlib.sha256('password'.encode()).hexdigest()

	# Test unique email
	result = UserService.register_user('test2', 'test@test.com', 'password2')
	assert result == 'Email already exists'

	# Test password hashing
	UserService.register_user('test3', 'test3@test.com', 'password3')
	assert UserService.users_db['test3@test.com'].password != 'password3'

def test_login_user():
	# Test successful login
	result = UserService.login_user('test@test.com', 'password')
	assert result == 'User logged in successfully'

	# Test non-existent user
	result = UserService.login_user('nonexistent@test.com', 'password')
	assert result == 'User does not exist'

	# Test incorrect password
	result = UserService.login_user('test@test.com', 'wrongpassword')
	assert result == 'Incorrect password'

def test_reset_password():
	# Test successful password reset
	UserService.reset_password('test@test.com', 'newpassword')
	assert UserService.users_db['test@test.com'].password == hashlib.sha256('newpassword'.encode()).hexdigest()

	# Test non-existent user
	result = UserService.reset_password('nonexistent@test.com', 'newpassword')
	assert result == 'User does not exist'
