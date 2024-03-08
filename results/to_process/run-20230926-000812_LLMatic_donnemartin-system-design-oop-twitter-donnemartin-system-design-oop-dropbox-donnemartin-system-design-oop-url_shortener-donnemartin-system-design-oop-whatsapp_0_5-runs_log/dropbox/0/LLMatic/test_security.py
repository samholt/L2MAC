import pytest
from security import Security


def test_encryption_decryption():
	security = Security()
	data = b'some data'
	encrypted_data = security.encrypt(data)
	assert data != encrypted_data
	decrypted_data = security.decrypt(encrypted_data)
	assert data == decrypted_data


def test_activity_log():
	Security.log_activity('user1', 'uploaded file')
	Security.log_activity('user1', 'downloaded file')
	Security.log_activity('user2', 'shared file')
	assert Security.get_activity('user1') == ['uploaded file', 'downloaded file']
	assert Security.get_activity('user2') == ['shared file']
	assert Security.get_activity('user3') == []
