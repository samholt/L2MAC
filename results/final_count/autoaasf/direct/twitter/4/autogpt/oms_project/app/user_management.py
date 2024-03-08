import hashlib


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, password):
        return self.password == self.hash_password(password)


def register_user(username, password, email):
    user = User(username, password, email)
    # TODO: Save user to database
    return user


def authenticate_user(username, password):
    # TODO: Retrieve user from database
    user = None
    if user and user.verify_password(password):
        return user
    return None
