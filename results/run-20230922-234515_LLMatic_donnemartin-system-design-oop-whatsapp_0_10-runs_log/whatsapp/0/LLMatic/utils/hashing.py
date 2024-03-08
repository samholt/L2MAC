import hashlib
import secrets


def hash_password(password: str) -> str:
	# Use the SHA256 hash algorithm
	return hashlib.sha256(password.encode()).hexdigest()


def generate_password_reset_token() -> str:
	# Generate a random 32-byte string and convert it to a 64-character hexadecimal string
	return secrets.token_hex(32)
