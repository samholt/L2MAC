import pytest
from security import Security

security_manager = Security()

@pytest.mark.parametrize('user_id, user_data', [(1, {'name': 'John Doe', 'email': 'john@example.com'})])
def test_protect_user_data(user_id, user_data):
	assert security_manager.protect_user_data(user_id, user_data) == 'User data protected'

@pytest.mark.parametrize('user_id', [1])
def test_ensure_privacy(user_id):
	assert security_manager.ensure_privacy(user_id) == 'User privacy ensured'

@pytest.mark.parametrize('user_id, payment_data', [(1, {'card_number': '1234567812345678', 'expiry_date': '01/23', 'cvv': '123'})])
def test_secure_payment_gateway(user_id, payment_data):
	assert security_manager.secure_payment_gateway(user_id, payment_data) == 'Payment gateway secured'
