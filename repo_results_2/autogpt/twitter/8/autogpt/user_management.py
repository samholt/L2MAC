import hashlib

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.profile = {}
        self.privacy_settings = {}

    # Method to hash password
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    # Method to check password
    def check_password(self, password):
        return self.password == self.hash_password(password)

    # Method to update profile
    def update_profile(self, profile):
        self.profile = profile

    # Method to update privacy settings
    def update_privacy_settings(self, privacy_settings):
        self.privacy_settings = privacy_settings