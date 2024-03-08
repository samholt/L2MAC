import pytest
import auth

@pytest.fixture(autouse=True)
def clear_database():
	auth.users_db.clear()
	auth.password_reset_tokens.clear()


def test_hash_password():
	assert auth.hash_password('password') == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'


def test_signup():
	assert auth.signup('test@example.com', 'password') == 'User registered successfully'
	assert auth.signup('test@example.com', 'password') == 'User already exists'


def test_login():
	auth.signup('test@example.com', 'password')
	assert auth.login('test@example.com', 'password') == 'Login successful'
	assert auth.login('test@example.com', 'wrong_password') == 'Invalid email or password'
	assert auth.login('wrong@example.com', 'password') == 'Invalid email or password'


def test_generate_password_reset_link():
	auth.signup('test@example.com', 'password')
	link = auth.generate_password_reset_link('test@example.com')
	assert 'www.example.com/reset_password?token=' in link
	assert auth.generate_password_reset_link('wrong@example.com') == 'User does not exist'


def test_reset_password():
	auth.signup('test@example.com', 'password')
	link = auth.generate_password_reset_link('test@example.com')
	token = link.split('=')[1]
	assert auth.reset_password(token, 'new_password') == 'Password updated successfully'
	assert auth.login('test@example.com', 'new_password') == 'Login successful'
	assert auth.reset_password('wrong_token', 'new_password') == 'Invalid token'
