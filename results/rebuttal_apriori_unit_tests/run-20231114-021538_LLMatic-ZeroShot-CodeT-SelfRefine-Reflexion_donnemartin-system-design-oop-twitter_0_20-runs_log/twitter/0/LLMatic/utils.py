import hashlib

def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password, provided_password):
	return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()
