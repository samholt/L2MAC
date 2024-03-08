import pytest
from cloudsafe.app.security_service import SecurityService
from cryptography.fernet import Fernet


def test_encrypt_decrypt_file():
	# Generate a secret key
	secret_key = Fernet.generate_key()

	# Initialize the SecurityService
	security_service = SecurityService(secret_key)

	# Test file encryption and decryption
	file = b'This is a test file.'
	encrypted_file = security_service.encrypt_file(file)
	decrypted_file = security_service.decrypt_file(encrypted_file)

	assert decrypted_file == file


def test_log_activity():
	# Initialize the SecurityService
	security_service = SecurityService(Fernet.generate_key())

	# Test activity logging
	user_id = 1
	action = 'Uploaded a file.'
	activity_log = security_service.log_activity(user_id, action)

	assert activity_log.user_id == user_id
	assert activity_log.action == action
