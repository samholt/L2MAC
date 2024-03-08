import security
import pytest


def test_encrypt_decrypt():
	# Test encryption and decryption
	file = b'This is a test file'
	encrypted_file = security.encrypt_file(file)
	decrypted_file = security.decrypt_file(encrypted_file)
	assert decrypted_file == file


def test_log_activity():
	# Test activity logging
	user_id = 'user1'
	activity = 'Uploaded a file'
	assert security.log_activity(user_id, activity) == True
	assert len(security.activity_log[user_id]) == 1
	assert security.activity_log[user_id][0]['activity'] == activity
