class UserProfile:
    def __init__(self, user, display_name, status):
        self.user = user
        self.display_name = display_name
        self.status = status

    def update_display_name(self, new_display_name):
        self.display_name = new_display_name

    def update_status(self, new_status):
        self.status = new_status


def create_user_profile(user, display_name, status):
    return UserProfile(user, display_name, status)