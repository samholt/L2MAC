import hashlib
import os
import binascii

# Mock database
user_data = {}


def hash_password(password):
	"""Hash a password for storing."""
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	hashed_password = binascii.hexlify(hashed_password)
	return (salt + hashed_password).decode('ascii')


def verify_password(stored_password, provided_password):
	"""Verify a stored password against one provided by user"""
	salt = stored_password[:64]
	stored_password = stored_password[64:]
	hashed_password = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
	hashed_password = binascii.hexlify(hashed_password).decode('ascii')
	return hashed_password == stored_password


def store_user_data(user_id, password):
	"""Store user data securely"""
	user_data[user_id] = hash_password(password)


def check_user_data(user_id, password):
	"""Check user data"""
	if user_id in user_data:
		return verify_password(user_data[user_id], password)
	return False
