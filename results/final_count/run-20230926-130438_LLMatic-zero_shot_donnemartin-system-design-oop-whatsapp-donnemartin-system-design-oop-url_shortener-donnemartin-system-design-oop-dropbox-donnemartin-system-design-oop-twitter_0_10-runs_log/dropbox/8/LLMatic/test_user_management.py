import pytest
from user_management import User, UserProfile, register, login, forgot_password, get_profile, change_password, users_db

def test_register_new_user():
	user = User('Test User', 'test@example.com', 'password')
	assert register(user) == 'Registration successful'
	assert users_db[user.email] == user

def test_register_duplicate_user():
	user = User('Test User', 'test@example.com', 'password')
	register(user)
	assert register(user) == 'User already exists'

def test_login():
	user = User('Test User', 'test@example.com', 'password')
	register(user)
	assert login(user.email, user.password) == 'Login successful'
	assert login('invalid@example.com', 'password') == 'Invalid email or password'
	assert login(user.email, 'wrongpassword') == 'Invalid email or password'

def test_forgot_password():
	user = User('Test User', 'test@example.com', 'password')
	register(user)
	assert forgot_password(user.email) == 'Password reset link sent'
	assert forgot_password('invalid@example.com') == 'Email not found'

def test_get_profile():
	user = User('Test User', 'test@example.com', 'password')
	register(user)
	profile = get_profile(user)
	assert isinstance(profile, UserProfile)
	assert profile.name == user.name
	assert profile.email == user.email
	assert profile.storage_used == 0
	assert profile.storage_remaining == 100

def test_change_password():
	user = User('Test User', 'test@example.com', 'password')
	register(user)
	assert change_password(user, 'newpassword') == 'Password changed successfully'
	assert users_db[user.email].password == 'newpassword'
	assert change_password(User('Invalid User', 'invalid@example.com', 'password'), 'newpassword') == 'User not found'
