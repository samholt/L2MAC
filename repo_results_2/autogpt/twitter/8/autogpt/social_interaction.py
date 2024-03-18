class SocialInteraction:
    def __init__(self):
        self.following = set()
        self.followers = set()
        self.messages = []
        self.notifications = []

    # Method to follow a user
    def follow(self, user):
        self.following.add(user)
        user.followers.add(self)

    # Method to unfollow a user
    def unfollow(self, user):
        self.following.remove(user)
        user.followers.remove(self)

    # Method to send a message
    def send_message(self, user, message):
        self.messages.append((user, message))
        user.notifications.append((self, message))

    # Method to read notifications
    def read_notifications(self):
        notifications = self.notifications
        self.notifications = []
        return notifications