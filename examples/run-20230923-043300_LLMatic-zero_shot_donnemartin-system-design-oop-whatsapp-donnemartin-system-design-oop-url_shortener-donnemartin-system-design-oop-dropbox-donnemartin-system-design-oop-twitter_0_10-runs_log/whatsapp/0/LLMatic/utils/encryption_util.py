from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt(message):
	return cipher_suite.encrypt(message.encode())

def decrypt(token):
	return cipher_suite.decrypt(token).decode()
