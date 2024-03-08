import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password):
        return self.password == self.hash_password(password)


class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        return True

    def authenticate_user(self, username, password):
        if username not in self.users:
            return False
        return self.users[username].check_password(password)