from cryptography.fernet import Fernet
import datetime

# Mock database
activity_log = {}

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt_file(file):
	# Encrypt the file
	encrypted_file = cipher_suite.encrypt(file)
	return encrypted_file


def decrypt_file(encrypted_file):
	# Decrypt the file
	decrypted_file = cipher_suite.decrypt(encrypted_file)
	return decrypted_file


def log_activity(user_id, activity):
	# Log user activity
	if user_id not in activity_log:
		activity_log[user_id] = []
	activity_log[user_id].append({
		'activity': activity,
		'time': datetime.datetime.now()
	})
	return True
