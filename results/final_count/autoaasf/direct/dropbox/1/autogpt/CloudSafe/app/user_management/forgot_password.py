from .user import User


def reset_password(email, new_password):
    # TODO: Retrieve the user from the database
    user = None
    if user:
        user.change_password(new_password)
        # TODO: Save the updated user to the database
        return True
    else:
        return False