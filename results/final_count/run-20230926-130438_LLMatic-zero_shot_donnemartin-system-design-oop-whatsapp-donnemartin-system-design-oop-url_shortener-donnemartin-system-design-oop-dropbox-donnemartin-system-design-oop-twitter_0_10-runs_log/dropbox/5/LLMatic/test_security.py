import security


def test_encryption_decryption():
	key = security.generate_key()
	content = b'This is some test content'
	cipher_text = security.encrypt_file_content(key, content)
	decrypted_content = security.decrypt_file_content(key, cipher_text)
	assert content == decrypted_content


def test_add_log_entry():
	user = 'test_user'
	action = 'test_action'
	log_entry = security.add_log_entry(user, action)
	assert log_entry in security.log_db[user]
