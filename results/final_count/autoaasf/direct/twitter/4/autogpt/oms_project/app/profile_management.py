class UserProfile:
    def __init__(self, user, display_name, bio, profile_picture):
        self.user = user
        self.display_name = display_name
        self.bio = bio
        self.profile_picture = profile_picture

    def update_display_name(self, new_display_name):
        self.display_name = new_display_name

    def update_bio(self, new_bio):
        self.bio = new_bio

    def update_profile_picture(self, new_profile_picture):
        self.profile_picture = new_profile_picture


def create_user_profile(user, display_name, bio, profile_picture):
    profile = UserProfile(user, display_name, bio, profile_picture)
    # TODO: Save user profile to database
    return profile


def update_user_profile(user, new_display_name=None, new_bio=None, new_profile_picture=None):
    # TODO: Retrieve user profile from database
    profile = None
    if new_display_name:
        profile.update_display_name(new_display_name)
    if new_bio:
        profile.update_bio(new_bio)
    if new_profile_picture:
        profile.update_profile_picture(new_profile_picture)
    # TODO: Save updated user profile to database
    return profile
