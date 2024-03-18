class SocialInteraction:
    def __init__(self):
        self.followers = []
        self.following = []

    def follow(self, user):
        self.following.append(user)
        user.followers.append(self)

    def send_direct_message(self, user, message):
        # This method should be implemented to allow users to send direct messages
        pass

    def receive_notification(self, notification):
        # This method should be implemented to allow users to receive notifications
        pass