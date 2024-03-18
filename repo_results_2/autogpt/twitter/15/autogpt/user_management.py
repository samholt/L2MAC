import hashlib

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.profile = {}

    # Hash password for security
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Check if entered password is correct
    def check_password(self, password):
        return self.password == self.hash_password(password)

    # Update profile
    def update_profile(self, profile):
        self.profile.update(profile)

# User management class
class UserManagement:
    def __init__(self):
        self.users = {}

    # Register new user
    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        return True

    # Authenticate user
    def authenticate(self, username, password):
        if username not in self.users:
            return False
        return self.users[username].check_password(password)

    # Update user profile
    def update_profile(self, username, profile):
        if username not in self.users:
            return False
        self.users[username].update_profile(profile)
        return True