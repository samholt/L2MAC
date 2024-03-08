import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()
	user_accounts.create_profile('user1', {'name': 'John Doe'})
	assert user_accounts.get_profile('user1') == {'name': 'John Doe'}
	user_accounts.customize_profile('user1', {'name': 'John Doe', 'age': 30})
	assert user_accounts.get_profile('user1') == {'name': 'John Doe', 'age': 30}
	user_accounts.save_event('user1', 'event1')
	assert user_accounts.get_events('user1') == ['event1']
