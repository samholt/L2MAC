import hashlib
import uuid

# Mock database
users_db = {}
password_reset_tokens = {}


def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def signup(email, password):
	if email in users_db:
		return 'User already exists'
	else:
		users_db[email] = hash_password(password)
		return 'User registered successfully'


def login(email, password):
	if email in users_db and users_db[email] == hash_password(password):
		return 'Login successful'
	else:
		return 'Invalid email or password'


def generate_password_reset_link(email):
	if email not in users_db:
		return 'User does not exist'
	else:
		token = str(uuid.uuid4())
		password_reset_tokens[token] = email
		return f'Password reset link: www.example.com/reset_password?token={token}'


def reset_password(token, new_password):
	if token not in password_reset_tokens:
		return 'Invalid token'
	else:
		email = password_reset_tokens[token]
		users_db[email] = hash_password(new_password)
		return 'Password updated successfully'
