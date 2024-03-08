from cloudsafe.controllers.user_controller import register, login, profile, forgot_password


def test_register():
	assert register() == 'Register'

def test_login():
	assert login() == 'Login'

def test_profile():
	assert profile() == 'Profile'

def test_forgot_password():
	assert forgot_password() == 'Forgot Password'
