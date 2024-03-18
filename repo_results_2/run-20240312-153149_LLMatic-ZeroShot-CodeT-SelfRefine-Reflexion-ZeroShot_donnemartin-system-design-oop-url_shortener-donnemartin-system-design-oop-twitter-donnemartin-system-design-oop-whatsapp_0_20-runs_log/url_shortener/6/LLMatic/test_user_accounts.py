import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	ua = UserAccounts()

	# Test account creation
	assert ua.create_account('user1', 'pass1') == True
	assert ua.create_account('user1', 'pass2') == False

	# Test login
	assert ua.login('user1', 'pass1') == True
	assert ua.login('user1', 'wrongpass') == False

	# Test logout
	assert ua.logout('user1') == True
	assert ua.logout('user2') == False

	# Test view urls
	assert ua.view_urls('user1') == []
	assert ua.view_urls('user2') == None
