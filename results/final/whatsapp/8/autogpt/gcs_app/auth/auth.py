from typing import Tuple


class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email


def register_user(username: str, password: str, email: str) -> User:
    user = User(username, password, email)
    return user


def authenticate_user(username: str, password: str, users: list[User]) -> Tuple[bool, str]:
    for user in users:
        if user.username == username:
            if user.password == password:
                return True, 'Authenticated'
            else:
                return False, 'Incorrect password'
    return False, 'User not found'