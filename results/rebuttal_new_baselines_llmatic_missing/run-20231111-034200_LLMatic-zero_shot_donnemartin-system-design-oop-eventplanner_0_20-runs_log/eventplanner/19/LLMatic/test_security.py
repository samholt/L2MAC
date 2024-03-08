import pytest
from security import Security

def test_protect_user_data():
	security = Security()
	assert security.protect_user_data('user1', {'name': 'John', 'email': 'john@example.com'}) == 'User data protected'

def test_maintain_privacy():
	security = Security()
	security.protect_user_data('user1', {'name': 'John', 'email': 'john@example.com'})
	assert security.maintain_privacy('user1') == 'Privacy maintained'

def test_secure_transaction():
	security = Security()
	assert security.secure_transaction('trans1', {'amount': 100, 'currency': 'USD'}) == 'Transaction secured'
