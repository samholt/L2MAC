import hashlib
import binascii
import os

# Mock database
user_data = {}


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


def store_user_data(user_id, password):
	"""Store user data in the mock database"""
	user_data[user_id] = hash_password(password)


def check_user_data(user_id, password):
	"""Check user data in the mock database"""
	if user_id in user_data:
		return verify_password(user_data[user_id], password)
	return False
