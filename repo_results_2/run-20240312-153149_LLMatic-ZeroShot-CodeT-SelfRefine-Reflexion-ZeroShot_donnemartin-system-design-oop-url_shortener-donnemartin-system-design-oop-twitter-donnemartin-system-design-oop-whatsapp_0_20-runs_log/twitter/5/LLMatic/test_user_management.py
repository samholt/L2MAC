import pytest
from user_management import register_user, authenticate_user, reset_password, edit_profile, toggle_visibility, users_db

def test_register_user():
	users_db.clear()
	assert register_user('testuser', 'testpassword') == {'message': 'User registered successfully'}
	assert 'testuser' in users_db


def test_authenticate_user():
	users_db.clear()
	register_user('testuser', 'testpassword')
	assert 'token' in authenticate_user('testuser', 'testpassword')
	assert authenticate_user('testuser', 'wrongpassword') == {'message': 'Invalid username or password'}
	assert authenticate_user('wronguser', 'testpassword') == {'message': 'Invalid username or password'}


def test_reset_password():
	users_db.clear()
	register_user('testuser', 'testpassword')
	assert reset_password('testuser', 'newpassword') == {'message': 'Password reset successfully'}
	assert 'token' in authenticate_user('testuser', 'newpassword')
	assert authenticate_user('testuser', 'testpassword') == {'message': 'Invalid username or password'}


def test_edit_profile():
	users_db.clear()
	register_user('testuser', 'testpassword')
	assert edit_profile('testuser', {'name': 'Test User', 'email': 'testuser@example.com'}) == {'message': 'Profile updated successfully'}
	assert users_db['testuser']['profile'] == {'name': 'Test User', 'email': 'testuser@example.com'}


def test_toggle_visibility():
	users_db.clear()
	register_user('testuser', 'testpassword')
	assert toggle_visibility('testuser') == {'message': 'Profile visibility toggled'}
	assert not users_db['testuser']['visible']
	assert toggle_visibility('testuser') == {'message': 'Profile visibility toggled'}
	assert users_db['testuser']['visible']
