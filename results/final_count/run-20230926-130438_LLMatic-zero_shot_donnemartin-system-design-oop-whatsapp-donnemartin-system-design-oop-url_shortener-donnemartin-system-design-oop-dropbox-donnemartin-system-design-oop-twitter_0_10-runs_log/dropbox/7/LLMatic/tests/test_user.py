import pytest
from models.user import User
from services.user_service import register_user, login_user, forgot_password, get_profile, change_password, log_activity, users_db

def test_user():
	user = User('1', 'Test User', 'test@example.com', 'password', 'http://example.com/profile.jpg', 0)

	assert user.get_id() == '1'
	assert user.get_name() == 'Test User'
	assert user.get_email() == 'test@example.com'
	assert user.get_password() == 'password'
	assert user.get_profile_picture() == 'http://example.com/profile.jpg'
	assert user.get_storage_used() == 0

	user.set_name('New Name')
	assert user.get_name() == 'New Name'

	user.set_email('new@example.com')
	assert user.get_email() == 'new@example.com'

	user.set_password('newpassword')
	assert user.get_password() == 'newpassword'

	user.set_profile_picture('http://newexample.com/profile.jpg')
	assert user.get_profile_picture() == 'http://newexample.com/profile.jpg'

	user.set_storage_used(100)
	assert user.get_storage_used() == 100

def test_register_user():
	# Register a user
	register_user('Test User', 'test@example.com', 'password')
	
	# Check that the user is added to the database
	assert 'test@example.com' in users_db
	
	# Check that the email is unique
	assert register_user('Test User', 'test@example.com', 'password') == 'Email already in use'

def test_login_user():
	# Login a user
	user = login_user('test@example.com', 'password')
	
	# Check that the correct user is returned
	assert user.get_email() == 'test@example.com'
	
	# Check that the password is correct
	assert user.get_password() == 'password'
	
	# Check invalid login
	assert login_user('test@example.com', 'wrongpassword') == 'Invalid email or password'
	assert login_user('wrong@example.com', 'password') == 'Invalid email or password'

def test_forgot_password():
	# Forgot password
	temp_password = forgot_password('test@example.com')
	
	# Check that the password is changed
	assert users_db['test@example.com'].get_password() == temp_password
	
	# Check invalid email
	assert forgot_password('wrong@example.com') == 'Email not found'

def test_get_profile():
	# Get profile
	profile = get_profile('test@example.com')
	
	# Check that the correct profile is returned
	assert profile['name'] == 'Test User'
	assert profile['email'] == 'test@example.com'
	assert profile['profile_picture'] == None
	assert profile['storage_used'] == 0
	
	# Check invalid email
	assert get_profile('wrong@example.com') == 'User not found'

def test_change_password():
	# Change password
	assert change_password('test@example.com', 'newpassword') == 'Password changed successfully'
	
	# Check that the password is changed
	assert users_db['test@example.com'].get_password() == 'newpassword'
	
	# Check invalid email
	assert change_password('wrong@example.com', 'newpassword') == 'User not found'

def test_log_activity():
	# Log activity
	activity_log = log_activity('test@example.com', 'upload')
	
	# Check that the action is added to the activity log
	assert 'upload' in activity_log
	
	# Check invalid email
	assert log_activity('wrong@example.com', 'upload') == 'User not found'
