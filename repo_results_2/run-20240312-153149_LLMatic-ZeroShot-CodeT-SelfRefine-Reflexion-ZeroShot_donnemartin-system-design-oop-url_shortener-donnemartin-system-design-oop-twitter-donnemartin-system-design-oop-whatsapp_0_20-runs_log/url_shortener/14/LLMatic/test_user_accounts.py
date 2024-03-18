import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test registration
	assert user_accounts.register('user1', 'password1') == True
	assert user_accounts.register('user1', 'password2') == False

	# Test login
	assert user_accounts.login('user1', 'password1') == True
	assert user_accounts.login('user1', 'password2') == False
	assert user_accounts.login('user2', 'password1') == False

	# Test URL management
	assert user_accounts.add_url('user1', 'url1') == True
	assert user_accounts.get_urls('user1') == ['url1']
	assert user_accounts.add_url('user2', 'url2') == False
	assert user_accounts.get_urls('user2') == None
