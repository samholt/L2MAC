from Crypto.Cipher import AES
import os

# Fixed key for testing
key = os.urandom(16)

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

# Function to decrypt file
def decrypt_file(filename, key):
    # Read encrypted data from file
    with open(filename, 'rb') as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    # Create AES cipher with key and nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Decrypt data
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # Write decrypted data to file
    with open(filename, 'wb') as file:
        file.write(data)

    # Return success message
    return 'File decrypted successfully'

# Test functions with dummy file and fixed key
print(encrypt_file('test.txt', key))
print(decrypt_file('test.txt', key))