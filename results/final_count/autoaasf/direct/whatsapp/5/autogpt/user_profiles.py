class UserProfile:

    def __init__(self, user_id, username, email, display_name=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.display_name = display_name if display_name else username

    def update_profile(self, username=None, email=None, display_name=None):
        if username:
            self.username = username
        if email:
            self.email = email
        if display_name:
            self.display_name = display_name


if __name__ == '__main__':
    user_profile = UserProfile(1, 'test_user', 'test@example.com')
    user_profile.update_profile(display_name='Test User')