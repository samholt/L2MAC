import pytest
from main import Application
from user import User


def test_application():
	app = Application()
	app.register('test_user', 'password')
	assert 'test_user' in app.users
	assert app.login('test_user', 'password') == 'Login successful'
	assert app.is_logged_in('test_user') == True
	assert app.logout('test_user') == 'Logout successful'
	assert app.is_logged_in('test_user') == False
