# User Profile Module

class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.profile_picture = None
        self.status_message = ''
        self.privacy_settings = {'user_details': 'public', 'last_seen': 'public'}

    # Profile Picture
    def upload_picture(self, picture):
        # Validate the uploaded picture
        if not validate_picture(picture):
            return 'Invalid picture'
        # Store the picture securely
        self.profile_picture = store_picture(picture)
        return 'Picture uploaded successfully'

    # Status Message
    def set_status_message(self, message):
        # Validate the status message
        if not validate_message(message):
            return 'Invalid message'
        # Store the status message
        self.status_message = message
        return 'Status message set successfully'

    # Privacy Settings
    def configure_privacy_settings(self, settings):
        # Validate the privacy settings
        if not validate_settings(settings):
            return 'Invalid settings'
        # Store the privacy settings
        self.privacy_settings = settings
        return 'Privacy settings configured successfully'