from cryptography.fernet import Fernet


class Encryption:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_message(key, message):
        f = Fernet(key)
        return f.encrypt(message.encode()).decode()

    @staticmethod
    def decrypt_message(key, encrypted_message):
        f = Fernet(key)
        return f.decrypt(encrypted_message.encode()).decode()