import security

def test_ensure_data_protection():
	security_obj = security.Security()
	security_obj.ensure_data_protection('user1', 'data1')
	assert security_obj.user_data['user1'] == 'data1'

def test_integrate_payment_gateway():
	security_obj = security.Security()
	security_obj.integrate_payment_gateway('payment1', 'payment_info1')
	assert security_obj.payment_gateway['payment1'] == 'payment_info1'
