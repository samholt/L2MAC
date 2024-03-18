import os

# User profile data storage
profiles = {}

# Set profile picture function
def set_profile_picture(user_id, picture_link):
    if user_id in profiles:
        profiles[user_id]['picture'] = picture_link
        return 'Profile picture set successfully.'
    else:
        return 'User not found.'

# Set status message function
def set_status_message(user_id, status_message):
    if user_id in profiles:
        profiles[user_id]['status'] = status_message
        return 'Status message set successfully.'
    else:
        return 'User not found.'

# Configure privacy settings function
def configure_privacy_settings(user_id, setting, value):
    if user_id in profiles:
        if setting in profiles[user_id]['privacy']:
            profiles[user_id]['privacy'][setting] = value
            return 'Privacy setting configured successfully.'
        else:
            return 'Invalid setting.'
    else:
        return 'User not found.'