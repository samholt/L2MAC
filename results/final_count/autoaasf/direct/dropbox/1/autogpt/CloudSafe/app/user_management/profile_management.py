from .user import User


def update_user_profile(user, new_username=None, new_email=None):
    if new_username:
        user.update_username(new_username)
    if new_email:
        user.update_email(new_email)
    # TODO: Save the updated user to the database
    return user