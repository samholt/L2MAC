import pytest
from security import Security


def test_encrypt_data():
	security = Security()
	data = 'test data'
	encrypted_data = security.encrypt_data(data)
	assert encrypted_data != data, 'Data is not encrypted'
	assert len(encrypted_data) == 64, 'SHA256 encrypted data should be 64 characters long'


def test_conduct_security_audit():
	security = Security()
	audit_result = security.conduct_security_audit()
	assert audit_result == 'Security audit conducted successfully', 'Security audit failed'
	assert len(security.audit_logs) == 1, 'Audit log not updated'

