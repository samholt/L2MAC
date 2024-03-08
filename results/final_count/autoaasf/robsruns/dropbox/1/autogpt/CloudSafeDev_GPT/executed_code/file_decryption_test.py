from cryptography.fernet import Fernet
import os

# Function to decrypt a file
def decrypt_file(filename, key):
    # Instantiate a Fernet instance with the key
    cipher_suite = Fernet(key)

    # Read the file
    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the file
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Write the decrypted data to the file
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

    return 'File decrypted successfully'