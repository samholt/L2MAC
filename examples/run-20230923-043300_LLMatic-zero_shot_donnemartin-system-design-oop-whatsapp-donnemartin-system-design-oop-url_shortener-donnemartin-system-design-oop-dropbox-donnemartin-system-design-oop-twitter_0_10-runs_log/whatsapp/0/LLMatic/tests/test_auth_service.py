from services.auth_service import AuthService

def test_register():
	AuthService.register('test@test.com', 'password')
	user = AuthService.login('test@test.com', 'password')
	assert user is not None
