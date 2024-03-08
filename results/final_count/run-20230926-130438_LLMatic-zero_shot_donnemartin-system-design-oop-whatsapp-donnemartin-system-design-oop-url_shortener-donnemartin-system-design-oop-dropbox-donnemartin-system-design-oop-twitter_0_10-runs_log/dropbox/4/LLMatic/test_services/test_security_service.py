from services.security_service import SecurityService


def test_log_activity():
	security_service = SecurityService()
	security_service.log_activity('user1', 'action1')
	logs = security_service.get_activity_logs('user1')
	assert len(logs) == 1
	assert str(logs[0]) == 'User: user1, Action: action1, Date/Time: ' + str(logs[0].date_time)


def test_encrypt_decrypt():
	security_service = SecurityService()
	data = 'test data'
	encrypted_data = security_service.encrypt(data)
	decrypted_data = security_service.decrypt(encrypted_data)
	assert decrypted_data == data
