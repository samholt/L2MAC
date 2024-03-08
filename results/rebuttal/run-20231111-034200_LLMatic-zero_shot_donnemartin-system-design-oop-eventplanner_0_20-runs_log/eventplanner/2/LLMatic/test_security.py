import pytest
from security import Security

def test_protect_user_data():
	security = Security()
	assert security.protect_user_data('user1', 'data1') == True
	assert security.get_user_data('user1') == 'data1'

def test_secure_payment():
	security = Security()
	assert security.secure_payment('user1', 'payment_info1') == True
	assert security.get_payment_info('user1') == 'payment_info1'
