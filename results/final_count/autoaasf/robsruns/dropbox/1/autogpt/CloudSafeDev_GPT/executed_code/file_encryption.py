from cryptography.fernet import Fernet
import os

# Function to encrypt a file
def encrypt_file(filename):
    # Generate a key and instantiate a Fernet instance
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Read the file
    with open(filename, 'rb') as file:
        file_data = file.read()

    # Encrypt the file
    encrypted_data = cipher_suite.encrypt(file_data)

    # Write the encrypted data to the file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

    return 'File encrypted successfully'