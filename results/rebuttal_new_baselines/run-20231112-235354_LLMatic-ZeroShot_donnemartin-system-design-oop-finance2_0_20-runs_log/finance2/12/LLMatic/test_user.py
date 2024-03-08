import pytest
from user import User

def test_user_creation():
	user = User()
	assert user.create_user('test', 'test') == 'User created successfully'
	assert user.create_user('test', 'test') == 'Username already exists'

def test_user_login():
	user = User()
	user.create_user('test', 'test')
	assert user.login('test', 'test') == 'Logged in successfully'
	assert user.login('test', 'wrong') == 'Invalid username or password'

def test_user_details_update():
	user = User()
	user.create_user('test', 'test')
	assert user.update_details('test', {'email': 'test@test.com'}) == 'Details updated successfully'
	assert user.update_details('wrong', {'email': 'test@test.com'}) == 'User not found'

def test_add_bank_account():
	user = User()
	user.create_user('test', 'test')
	assert user.add_bank_account('test', {'bank_name': 'Test Bank', 'account_number': '1234567890'}) == 'Bank account added successfully'
	assert user.add_bank_account('wrong', {'bank_name': 'Test Bank', 'account_number': '1234567890'}) == 'User not found'
