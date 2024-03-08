class SocialInteraction:
    def __init__(self, user):
        self.user = user
        self.following = []
        self.messages = []
        self.notifications = []

# Following & followers
def follow(user, other_user):
    user.following.append(other_user)

# Direct messaging
def send_message(user, other_user, message):
    user.messages.append((other_user, message))

# Notifications
def add_notification(user, notification):
    user.notifications.append(notification)