from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key=None):
        self.key = key if key else Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, message):
        return self.cipher_suite.encrypt(message.encode())

    def decrypt(self, encrypted_message):
        return self.cipher_suite.decrypt(encrypted_message).decode()
