class UserProfile:
    def __init__(self, user):
        self.user = user
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.bio = ''

    def update_profile(self, first_name=None, last_name=None, email=None, bio=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if bio:
            self.bio = bio


class ProfileManager:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, user):
        if user.username in self.profiles:
            return False
        self.profiles[user.username] = UserProfile(user)
        return True

    def get_profile(self, username):
        return self.profiles.get(username, None)

    def update_profile(self, username, first_name=None, last_name=None, email=None, bio=None):
        profile = self.get_profile(username)
        if profile:
            profile.update_profile(first_name, last_name, email, bio)
            return True
        return False