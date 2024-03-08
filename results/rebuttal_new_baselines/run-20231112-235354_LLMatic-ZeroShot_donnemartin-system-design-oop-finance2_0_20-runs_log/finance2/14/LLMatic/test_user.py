import app
from models.user import User

def test_user_authentication():
	user = User('test', 'test@test.com', 'password')
	assert user.authenticate('password') == True
	assert user.authenticate('wrong_password') == False

	with app.app.test_client() as c:
		response = c.post('/authenticate_user', json={'password': 'password'})
		assert response.status_code == 200
		assert response.get_json()['message'] == 'User authenticated, verification code sent'

		response = c.post('/authenticate_user', json={'password': 'wrong_password'})
		assert response.status_code == 401
		assert response.get_json()['message'] == 'Authentication failed'

def test_user_verification():
	user = User('test', 'test@test.com', 'password')
	user.send_verification_code()
	code = user.verification_code

	assert user.verify(code) == True
	assert user.verify(123456) == False

	with app.app.test_client() as c:
		response = c.post('/verify_user', json={'code': code, 'name': 'test'})
		assert response.status_code == 200
		assert response.get_json()['message'] == 'User verified'

		response = c.post('/verify_user', json={'code': 123456, 'name': 'test'})
		assert response.status_code == 401
		assert response.get_json()['message'] == 'Verification failed'
