import security


def test_generate_hash():
	"""Test the generate_hash function."""
	password = 'password123'
	hashed_password = security.generate_hash(password)
	assert len(hashed_password) == 64


def test_verify_password():
	"""Test the verify_password function."""
	password = 'password123'
	hashed_password = security.generate_hash(password)
	assert security.verify_password(hashed_password, password)
	assert not security.verify_password(hashed_password, 'wrongpassword')


def test_generate_key():
	"""Test the generate_key function."""
	key = security.generate_key()
	assert len(key) == 44


def test_encrypt_decrypt_data():
	"""Test the encrypt_data and decrypt_data functions."""
	key = security.generate_key()
	data = b'secret data'
	encrypted_data = security.encrypt_data(key, data)
	assert encrypted_data != data
	decrypted_data = security.decrypt_data(key, encrypted_data)
	assert decrypted_data == data
