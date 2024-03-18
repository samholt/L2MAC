

class PrivacySettings:
    def __init__(self, user):
        self.user = user
        self.settings = {'profile_public': True}

    def update_settings(self, **kwargs):
        self.settings.update(kwargs)

    def get_settings(self):
        return self.settings