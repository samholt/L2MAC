from .user import User


def login_user(username, password):
    # TODO: Retrieve the user from the database
    user = None
    if user and user.password == password:
        return user
    else:
        return None