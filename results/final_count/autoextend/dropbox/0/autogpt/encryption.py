from cryptography.fernet import Fernet


class Encryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher_suite.encrypt(data)

    def decrypt(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data)


if __name__ == '__main__':
    encryption = Encryption()
    data = b'Some data to be encrypted'
    encrypted_data = encryption.encrypt(data)
    decrypted_data = encryption.decrypt(encrypted_data)
    print('Data encrypted and decrypted successfully.')