import pytest
from security import Security


def test_protect_user_data():
	security = Security()
	user_id = 'user1'
	data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
	encrypted_data = security.protect_user_data(user_id, data)
	assert 'encrypted' in encrypted_data
	assert security.user_data[user_id] == encrypted_data


def test_handle_transaction():
	security = Security()
	user_id = 'user1'
	transaction = {'amount': 100, 'currency': 'USD'}
	handled_transaction = security.handle_transaction(user_id, transaction)
	assert handled_transaction == transaction
	assert security.transactions[user_id] == transaction
