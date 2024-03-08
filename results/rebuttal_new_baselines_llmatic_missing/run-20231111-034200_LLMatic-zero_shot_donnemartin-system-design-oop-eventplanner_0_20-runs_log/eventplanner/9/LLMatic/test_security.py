import security
import app

def test_password_hashing():
	password = 'password'
	password_hash = security.hash_password(password)
	assert security.check_password(password_hash, password)


def test_auth_token():
	user_id = 1
	token = security.generate_auth_token(user_id)
	assert security.verify_auth_token(token) == user_id


def test_mock_payment_gateway():
	assert security.mock_payment_gateway(100) == True
	assert security.mock_payment_gateway(0) == False
