import pytest
import user_accounts

def test_create_account():
	user = user_accounts.create_account('John Doe', 'Rock')
	assert user.name == 'John Doe'
	assert user.preferences == 'Rock'
	assert user.event_history == []

def test_delete_account():
	user_accounts.create_account('John Doe', 'Rock')
	user_accounts.delete_account('John Doe')
	assert user_accounts.get_account('John Doe') is None

def test_update_account():
	user_accounts.create_account('John Doe', 'Rock')
	user_accounts.update_account('John Doe', 'Pop')
	assert user_accounts.get_account('John Doe').preferences == 'Pop'

def test_get_account():
	user_accounts.create_account('John Doe', 'Rock')
	assert user_accounts.get_account('John Doe').name == 'John Doe'
