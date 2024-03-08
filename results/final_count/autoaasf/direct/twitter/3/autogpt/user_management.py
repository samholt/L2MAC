import hashlib
import secrets


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


def register(username, email, password):
    user = User(username, email, password)
    # Save user to database (to be implemented)
    return user


def authenticate(username, password):
    # Retrieve user from database (to be implemented)
    user = None
    if user and user.password == User.hash_password(password):
        return user
    return None


def update_profile(user, new_username=None, new_email=None):
    if new_username:
        user.username = new_username
    if new_email:
        user.email = new_email
    # Update user in database (to be implemented)
    return user


def generate_password_reset_token():
    return secrets.token_hex(32)


def reset_password(user, new_password, token):
    # Verify token (to be implemented)
    user.password = User.hash_password(new_password)
    # Update user in database (to be implemented)
    return user
