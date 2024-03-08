import pytest
from web_application import WebApplication
from user import User


def test_web_application():
	web_app = WebApplication()

	# Test manage_connectivity method
	web_app.manage_connectivity(True)
	assert web_app.online_status == True

	web_app.manage_connectivity(False)
	assert web_app.online_status == False

	# Test get_current_user and set_current_user methods
	user = User('test@example.com', 'password')
	web_app.set_current_user(user)
	assert web_app.get_current_user() == user
