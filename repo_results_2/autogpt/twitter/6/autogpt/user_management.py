
class UserProfile:
    def __init__(self, user, name, email, bio):
        self.user = user
        self.name = name
        self.email = email
        self.bio = bio

class PrivacySettings:
    def __init__(self, user, can_see_profile, can_see_posts):
        self.user = user
        self.can_see_profile = can_see_profile
        self.can_see_posts = can_see_posts

UserManager:
    def create_profile(self, user, name, email, bio):
        return UserProfile(user, name, email, bio)

    def set_privacy_settings(self, user, can_see_profile, can_see_posts):
        return PrivacySettings(user, can_see_profile, can_see_posts)