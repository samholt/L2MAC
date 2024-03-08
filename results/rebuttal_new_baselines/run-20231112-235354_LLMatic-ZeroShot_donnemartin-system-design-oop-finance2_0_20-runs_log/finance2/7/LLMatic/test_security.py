import security

def test_hash_password():
	assert len(security.hash_password('test_password')) == 64

def test_verify_password():
	stored_password = security.hash_password('test_password')
	assert security.verify_password(stored_password, 'test_password') == True

def test_generate_otp():
	assert len(security.generate_otp()) == 6
