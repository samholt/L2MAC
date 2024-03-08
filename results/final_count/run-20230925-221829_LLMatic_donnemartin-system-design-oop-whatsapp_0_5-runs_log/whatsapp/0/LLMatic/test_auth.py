import auth


def test_register_user():
	"""Test user registration."""
	email = 'test@example.com'
	password = 'password123'
	assert auth.register_user(email, password) == 'User registered successfully.'
	assert auth.register_user(email, password) == 'Email already registered.'


def test_generate_recovery_token():
	"""Test password recovery token generation."""
	email = 'test@example.com'
	assert isinstance(auth.generate_recovery_token(email), str)
	assert auth.generate_recovery_token('not_registered@example.com') == 'Email not registered.'
