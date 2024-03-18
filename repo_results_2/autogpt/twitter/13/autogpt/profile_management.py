class Profile:
    def __init__(self, user, bio='', privacy='public'):
        self.user = user
        self.bio = bio
        self.privacy = privacy

class ProfileManager:
    def update_bio(self, profile, bio):
        profile.bio = bio
        return profile
    def update_privacy(self, profile, privacy):
        profile.privacy = privacy
        return profile