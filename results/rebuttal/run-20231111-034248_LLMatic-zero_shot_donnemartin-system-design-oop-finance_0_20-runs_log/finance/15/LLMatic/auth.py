import hashlib
import binascii
import os

# Mock database
users_db = {}


def hash_password(password):
	"""Hash a password for storing."""
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	pwdhash = binascii.hexlify(pwdhash)
	return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
	"""Verify a stored password against one provided by user"""
	salt = stored_password[:64]
	stored_password = stored_password[64:]
	pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
	pwdhash = binascii.hexlify(pwdhash).decode('ascii')
	return pwdhash == stored_password


def register_user(username, password):
	if username in users_db:
		return False
	else:
		users_db[username] = hash_password(password)
		return True


def login_user(username, password):
	if username in users_db and verify_password(users_db[username], password):
		return True
	else:
		return False


def logout_user(username):
	if username in users_db:
		return True
	else:
		return False


def recover_password(username):
	# This is a mock function. In a real-world application, this should send an email to the user with a password reset link.
	if username in users_db:
		return True
	else:
		return False
