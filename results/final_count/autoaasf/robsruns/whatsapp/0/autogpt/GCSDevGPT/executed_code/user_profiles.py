class UserProfile:
    def __init__(self, user):
        self.user = user
        self.profile_info = {}

    def update_profile_info(self, key, value):
        self.profile_info[key] = value