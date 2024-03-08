from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt a file
def encrypt_file(file):
	with open(file, 'rb') as f:
		data = f.read()
	encrypted_data = cipher_suite.encrypt(data)
	with open(file, 'wb') as f:
		f.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file):
	with open(file, 'rb') as f:
		encrypted_data = f.read()
	data = cipher_suite.decrypt(encrypted_data)
	with open(file, 'wb') as f:
		f.write(data)
