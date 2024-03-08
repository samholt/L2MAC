from .user import User


def register_user(username, email, password):
    new_user = User(username, email, password)
    # TODO: Save the user to the database
    return new_user