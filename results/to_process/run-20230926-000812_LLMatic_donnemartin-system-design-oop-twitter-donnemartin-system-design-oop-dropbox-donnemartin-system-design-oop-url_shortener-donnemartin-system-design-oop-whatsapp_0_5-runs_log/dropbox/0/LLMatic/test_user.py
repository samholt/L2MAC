import user

def test_register():
	user.register('John Doe', 'johndoe@example.com', 'password')
	assert user.mock_db['johndoe@example.com'].name == 'John Doe'

def test_login():
	assert user.login('johndoe@example.com', 'password') == 'Login successful'
	assert user.login('johndoe@example.com', 'wrongpassword') == 'Invalid credentials'

def test_forgot_password():
	assert user.forgot_password('johndoe@example.com') == 'Password reset successful'
	assert user.login('johndoe@example.com', 'password') == 'Login successful'

def test_profile():
	profile = user.profile('johndoe@example.com')
	assert profile['name'] == 'John Doe'
	assert profile['email'] == 'johndoe@example.com'
	assert profile['profile_picture'] == 'default.jpg'
	assert profile['storage_used'] == 0
	assert profile['storage_remaining'] == 100

def test_change_password():
	assert user.change_password('johndoe@example.com', 'password', 'newpassword') == 'Password change successful'
	assert user.login('johndoe@example.com', 'newpassword') == 'Login successful'
