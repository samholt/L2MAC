from dataclasses import dataclass

# Mock database
users_db = {}

@dataclass
class User:
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None


def register_user(email: str, password: str) -> User:
	"""Register a new user."""
	if email in users_db:
		raise ValueError(f'User with email {email} already exists.')
	user = User(email, password)
	users_db[email] = user
	return user


def recover_password(email: str) -> str:
	"""Recover a user's password."""
	if email not in users_db:
		raise ValueError(f'User with email {email} does not exist.')
	return users_db[email].password


def set_profile_picture(email: str, picture: str):
	"""Set the user's profile picture."""
	if email not in users_db:
		raise ValueError(f'User with email {email} does not exist.')
	users_db[email].profile_picture = picture


def set_status_message(email: str, message: str):
	"""Set the user's status message."""
	if email not in users_db:
		raise ValueError(f'User with email {email} does not exist.')
	users_db[email].status_message = message


def set_privacy_settings(email: str, settings: dict):
	"""Set the user's privacy settings."""
	if email not in users_db:
		raise ValueError(f'User with email {email} does not exist.')
	users_db[email].privacy_settings = settings
