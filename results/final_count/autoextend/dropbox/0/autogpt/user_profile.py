class UserProfile:
    def __init__(self, user):
        self.user = user
        self.profile_picture = None
        self.storage_usage = 0

    def change_password(self, new_password):
        # Update user's password securely


if __name__ == '__main__':
    # Retrieve user data securely
    user = None  # Replace with retrieved user data
    user_profile = UserProfile(user)
    print(f'Name: {user_profile.user.name}')
    print(f'Email: {user_profile.user.email}')
    print(f'Storage Usage: {user_profile.storage_usage} MB')
    new_password = input('Enter new password: ')
    user_profile.change_password(new_password)
    print('Password changed successfully.')