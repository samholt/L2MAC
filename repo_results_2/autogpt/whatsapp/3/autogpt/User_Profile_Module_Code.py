class UserProfile:
    def __init__(self, user):
        self.user = user
        self.profile_picture = None
        self.status_message = ''
        self.privacy_settings = {'details': 'public', 'last_seen': 'public'}

    def upload_profile_picture(self, profile_picture):
        self.profile_picture = profile_picture

    def set_status_message(self, status_message):
        self.status_message = status_message

    def configure_privacy_settings(self, details, last_seen):
        self.privacy_settings['details'] = details
        self.privacy_settings['last_seen'] = last_seen

    def view_profile(self):
        profile = {'email': self.user.email, 'profile_picture': self.profile_picture, 'status_message': self.status_message}
        if self.privacy_settings['details'] == 'public':
            profile['details'] = self.user.details
        if self.privacy_settings['last_seen'] == 'public':
            profile['last_seen'] = self.user.last_seen
        return profile