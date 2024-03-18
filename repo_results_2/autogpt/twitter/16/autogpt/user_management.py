
class UserProfile:
    def __init__(self, user):
        self.user = user
        self.bio = ''
        self.privacy = 'public'

    def update_bio(self, bio):
        self.bio = bio

    def set_privacy(self, privacy):
        self.privacy = privacy


class ProfileManager:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, user):
        self.profiles[user.username] = UserProfile(user)

    def update_profile(self, username, bio):
        if username not in self.profiles:
            return 'User does not exist'
        self.profiles[username].update_bio(bio)
        return 'Profile updated successfully'

    def set_privacy(self, username, privacy):
        if username not in self.profiles:
            return 'User does not exist'
        self.profiles[username].set_privacy(privacy)
        return 'Privacy settings updated successfully'