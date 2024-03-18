import hashlib

# User Registration and Authentication

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == self.hash_password(password)