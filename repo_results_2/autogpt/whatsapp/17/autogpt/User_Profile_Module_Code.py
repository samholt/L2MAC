class UserProfile:
    def __init__(self, user):
        self.user = user
        self.profile_picture = None
        self.status_message = ''
        self.privacy_settings = {'user_details': 'public', 'last_seen': 'public'}

    def set_profile_picture(self, picture):
        self.profile_picture = picture

    def set_status_message(self, message):
        self.status_message = message

    def configure_privacy_settings(self, setting, value):
        if setting in self.privacy_settings:
            self.privacy_settings[setting] = value