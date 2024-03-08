import hashlib
import os
from cryptography.fernet import Fernet


def generate_hash(password):
	"""Generate a hashed password."""
	salt = os.urandom(32)
	password = password.encode()
	key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
	return salt + key


def verify_password(stored_password, provided_password):
	"""Verify a provided password against a stored salted password."""
	salt = stored_password[:32]
	stored_password = stored_password[32:]
	provided_password = provided_password.encode()
	key = hashlib.pbkdf2_hmac('sha256', provided_password, salt, 100000)
	return key == stored_password


def generate_key():
	"""Generate a symmetric encryption key."""
	return Fernet.generate_key()


def encrypt_data(key, data):
	"""Encrypt data with a given key."""
	cipher_suite = Fernet(key)
	encrypted_data = cipher_suite.encrypt(data)
	return encrypted_data


def decrypt_data(key, encrypted_data):
	"""Decrypt data with a given key."""
	cipher_suite = Fernet(key)
	decrypted_data = cipher_suite.decrypt(encrypted_data)
	return decrypted_data
