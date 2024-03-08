import hashlib
import os
import uuid


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, password):
        hashed_password, salt = self.password.split(':')
        return hashed_password == hashlib.sha256(salt.encode() + password.encode()).hexdigest()


def register(username, password):
    user = User(username, password)
    return user


def authenticate(user, password):
    return user.check_password(password)