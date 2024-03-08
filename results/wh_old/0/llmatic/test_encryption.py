from encryption import Encryption
def test_encryption():
    encryption = Encryption()
    message = 'Hello, User 2!'
    encrypted_message = encryption.encrypt(message)
    decrypted_message = encryption.decrypt(encrypted_message)
    assert message == decrypted_message
