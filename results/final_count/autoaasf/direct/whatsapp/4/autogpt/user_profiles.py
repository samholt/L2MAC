class UserProfile:
    def __init__(self, user, display_name, status, profile_picture):
        self.user = user
        self.display_name = display_name
        self.status = status
        self.profile_picture = profile_picture

    def update_display_name(self, new_display_name):
        self.display_name = new_display_name

    def update_status(self, new_status):
        self.status = new_status

    def update_profile_picture(self, new_profile_picture):
        self.profile_picture = new_profile_picture


class UserProfileManager:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, user, display_name, status, profile_picture):
        if user.username in self.profiles:
            return False
        self.profiles[user.username] = UserProfile(user, display_name, status, profile_picture)
        return True

    def get_profile(self, username):
        return self.profiles.get(username, None)