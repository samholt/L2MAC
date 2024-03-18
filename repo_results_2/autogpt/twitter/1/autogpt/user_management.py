import hashlib


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email
        self.profile = {}
        self.privacy_settings = {}

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, password):
        return self.password == self.hash_password(password)

    def update_profile(self, profile):
        self.profile = profile

    def update_privacy_settings(self, privacy_settings):
        self.privacy_settings = privacy_settings