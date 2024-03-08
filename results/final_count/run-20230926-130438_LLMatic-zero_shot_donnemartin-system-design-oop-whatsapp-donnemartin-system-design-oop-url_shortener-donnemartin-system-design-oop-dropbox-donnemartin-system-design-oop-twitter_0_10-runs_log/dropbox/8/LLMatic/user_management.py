from dataclasses import dataclass

# Mock database
users_db = {}

@dataclass
class User:
	name: str
	email: str
	password: str

@dataclass
class UserProfile:
	profile_picture: str
	name: str
	email: str
	storage_used: int
	storage_remaining: int


def register(user: User) -> str:
	"""Register a new user.

	:param user: User to register
	:return: Success message
	"""
	if user.email in users_db:
		return 'User already exists'
	users_db[user.email] = user
	return 'Registration successful'


def login(email: str, password: str) -> str:
	"""Login a user.

	:param email: User email
	:param password: User password
	:return: Success message
	"""
	if email in users_db and users_db[email].password == password:
		return 'Login successful'
	return 'Invalid email or password'


def forgot_password(email: str) -> str:
	"""Forgot password function.

	:param email: User email
	:return: Success message
	"""
	if email in users_db:
		return 'Password reset link sent'
	return 'Email not found'


def get_profile(user: User) -> UserProfile:
	"""Get user profile.

	:param user: User object
	:return: UserProfile object
	"""
	return UserProfile('default.png', user.name, user.email, 0, 100)


def change_password(user: User, new_password: str) -> str:
	"""Change user password.

	:param user: User object
	:param new_password: str
	:return: Success message
	"""
	if user.email in users_db:
		users_db[user.email].password = new_password
		return 'Password changed successfully'
	return 'User not found'
