import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test registration
	assert user_accounts.register('user1', 'password1') == True
	assert user_accounts.register('user1', 'password1') == False

	# Test login
	assert user_accounts.login('user1', 'password1') == True
	assert user_accounts.login('user1', 'wrongpassword') == False
	assert user_accounts.login('nonexistentuser', 'password1') == False

	# Test URL management
	assert user_accounts.add_url('user1', 'http://example.com') == True
	assert user_accounts.get_urls('user1') == ['http://example.com']
	assert user_accounts.add_url('nonexistentuser', 'http://example.com') == False
	assert user_accounts.get_urls('nonexistentuser') == None
