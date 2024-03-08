from Crypto.Cipher import AES
import os

# Function to encrypt file
def encrypt_file(filename, key):
    # Create AES cipher with key
    cipher = AES.new(key, AES.MODE_EAX)

    # Read file data
    with open(filename, 'rb') as file:
        data = file.read()

    # Encrypt data
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # Write encrypted data to file
    with open(filename, 'wb') as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

    # Return success message
    return 'File encrypted successfully'

# Test function with dummy file and key
print(encrypt_file('test.txt', os.urandom(16)))