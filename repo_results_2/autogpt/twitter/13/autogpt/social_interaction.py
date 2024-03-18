class SocialInteraction:
    def __init__(self, user):
        self.user = user
        self.following = []
        self.messages = []
        self.notifications = []

class SocialInteractionManager:
    def follow(self, user, other_user):
        user.following.append(other_user)
        return user
    def send_message(self, user, other_user, message):
        user.messages.append((other_user, message))
        return user
    def add_notification(self, user, notification):
        user.notifications.append(notification)
        return user