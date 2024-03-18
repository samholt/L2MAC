class PrivacySettings:
    def __init__(self, user):
        self.user = user
        self.public_profile = False
        self.public_posts = False

    def set_public_profile(self, public):
        self.public_profile = public

    def set_public_posts(self, public):
        self.public_posts = public