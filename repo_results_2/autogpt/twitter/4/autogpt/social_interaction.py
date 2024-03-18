# Social Interaction Code

# Following/Unfollowing Users
class Follow:
    def __init__(self, user, other_user):
        self.user = user
        self.other_user = other_user

    def follow_user(self):
        # Update database
        # Update user's timeline

    def unfollow_user(self):
        # Update database
        # Update user's timeline

# Timeline View
class Timeline:
    def __init__(self, user):
        self.user = user

    def view_timeline(self):
        # Return posts from followed users

# Direct Messaging
class DirectMessage:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message

    def send_message(self):
        # Store message in database

# Notifications
class Notification:
    def __init__(self, user):
        self.user = user

    def new_notification(self):
        # Create new notification

    def view_notifications(self):
        # Return notifications