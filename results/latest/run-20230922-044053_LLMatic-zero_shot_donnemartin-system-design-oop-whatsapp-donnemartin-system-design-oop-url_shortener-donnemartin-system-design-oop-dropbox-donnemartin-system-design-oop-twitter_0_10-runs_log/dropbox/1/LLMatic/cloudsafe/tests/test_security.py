import pytest
import os
from cloudsafe.security import encryption, activity_log

# Test file for encryption and decryption
file = 'test.txt'

# Write some data to the file
with open(file, 'wb') as f:
	f.write(b'Hello, World!')

# Test the encryption function
def test_encrypt_file():
	encryption.encrypt_file(file)
	with open(file, 'rb') as f:
		data = f.read()
	assert data != b'Hello, World!'

# Test the decryption function
def test_decrypt_file():
	encryption.decrypt_file(file)
	with open(file, 'rb') as f:
		data = f.read()
	assert data == b'Hello, World!'

# Test the activity log functionality
def test_activity_log():
	log = activity_log.ActivityLog()
	log.add_activity('user1', 'upload')
	log.add_activity('user2', 'download')
	assert log.get_activities('user1') == [(log.log[0][0], 'user1', 'upload')]
	assert log.get_activities('user2') == [(log.log[1][0], 'user2', 'download')]

# Delete the test file
os.remove(file)
